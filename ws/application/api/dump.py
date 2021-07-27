from flask.blueprints import Blueprint
from kafka import KafkaConsumer
import time
from threading import Thread
from application.blockchain import blockchain
import json
from flask_restful import Resource

blockchain_json_dump = Blueprint('jsonpage', __name__, template_folder='templates')

#kafka consumer
consumer = KafkaConsumer('transaction', bootstrap_servers=['143.107.232.252:9055'],
							auto_offset_reset='earliest', 
							enable_auto_commit=True,
							auto_commit_interval_ms=1000,
							group_id=None,
                			consumer_timeout_ms=30000)
lista_json = list()

#coleta as transações do kafka
def get_transactions_from_kafka():
	print("teste")
	print("conectou")
	for message in consumer:
		lista_json.append(json.loads(message.value.decode()))
		print(json.loads(message.value.decode()))

#coleta as transações do kafka através de uma API rest
@blockchain_json_dump.route('/jsondump', methods=['GET'])
def get_chain_api():
	t1 = Thread(target=get_transactions_from_kafka)
	t1.start()
	time.sleep(1)
	return json.dumps(lista_json[-20:])

#coleta as transações do kafka através do website
def get_chain():
	t1 = Thread(target=get_transactions_from_kafka)
	t1.start()
	time.sleep(1)
	return lista_json[-20:]

#retorna o json para um rest method ou para o WebServer
class Blockchain_api_dump(Resource):

	def get(self):
		return get_chain()
