# módulos de protótipos do nó da blockchain

from kafka import KafkaProducer
from kafka import KafkaConsumer
import time
from datetime import datetime
import random
import json
from threading import Thread

stop_flag = False

#lista de mensagens aleatórias para a transação
lista_msg = ["salve rapaziada", "bora discord", "cloud computing", "hj tem lasanha no bandeco","bcc melhor curso"]
list_types = ["transaction","create","payfee"]

dict_accounts = {"001":1000,"002":1000,"003":1000}
this_user = "001"


#cria uma transação aleatória
def create_transaction(parametro):
	valor = random.randint(1, 10)
	dest = random.choice(list(dict_accounts.keys()))
	while(this_user == dest):
		dest = random.choice(list(dict_accounts.keys()))
	transaction = dict()
	transaction['type'] = "transaction"
	transaction['remetente'] = this_user
	transaction['destinatario'] = dest
	transaction['mensagem'] = random.choice(lista_msg)
	
	transaction['timestamp'] = str(datetime.fromtimestamp(time.time())) 
	transaction['saldo_destinatario'] = dict_accounts[dest] + valor
	transaction['valor'] = valor
	transaction['saldo_remetente'] = dict_accounts[this_user] - valor
	transaction['double_spend'] = False
	transaction['block_index'] = 0
	return transaction


def consumer_func():
	consumer = KafkaConsumer('transaction', bootstrap_servers=['143.107.232.252:9055'],
							 auto_offset_reset='earliest', 
							 enable_auto_commit=True,
							 auto_commit_interval_ms=1000,
							 group_id=this_user,
                			consumer_timeout_ms=10000 #timeout
							 )
	#loop para rodar o consumer
	#o consumer tem um timeout de 10 segundos, caso não encontre nenhuma mensagem
	#o loop continua e verifica se a flag de parada foi ativada
	while True:
		if(stop_flag == True):
			return
			print("stop flag consumer")
		for message in consumer:
			transaction = json.loads(message.value)
			print("Received message:",transaction)
			dict_accounts[transaction["remetente"]] -= transaction['valor']
			dict_accounts[transaction["destinatario"]] += transaction['valor']

#função do produtor
def producer_func():
	global stop_flag # flag para parar o programa
	while(True):
		#uma transação é feita a cada 1m, 1m10s, 1m20s, 1m30s, ... , 2m.
		sleep_iters = 6 + random.randint(0,6)
		for i in range(sleep_iters):
			time.sleep(10)
			if(stop_flag == True):
				print("stop flag producer")
				break
		if(stop_flag == True):
			break
		producer = KafkaProducer(bootstrap_servers=['143.107.232.252:9055'])
		transaction = create_transaction(this_user)
		#caso ocorra algum erro e não retorne uma transação, 
		#trata o erro e reinicia o loop
		if(transaction == None):
			print("Um erro aconteceu")
			continue
		#checa se a transação é possível
		if(transaction['saldo_remetente'] < 0 or dict_accounts[this_user] < 0):
			print(transaction['saldo_remetente'],dict_accounts[this_user])
			print("Saldo insuficiente para enviar para outra conta ")
			continue
		#se tudo der certo, imprime na tela a transação e a envia pelo producer
		else:
			print("Sending transaction",json.dumps(transaction))
			producer.send('transaction', json.dumps(transaction).encode())

#inicia a thread do consumidor
t1 = Thread(target=consumer_func)
t1.start()
time.sleep(3)

#inicia a thread do produtor
t2 = Thread(target=producer_func,args=())
t2.start()
time.sleep(3)

# para parar o programa, digite stop no terminal e espere 10 segundos
while True:
	control = input("type \'stop\' to stop\n")
	if(control.strip() == "stop"):
		stop_flag = True
		print("Wait 10 seconds to shutdown")
		t1.join()
		t2.join()
		exit()






