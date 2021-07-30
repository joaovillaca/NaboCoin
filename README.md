# Trabalho de Blockchain + Cloud

Alunos:

- Bruno Gazoni 7585037
- Laura Genari 10801180
- luca botinha
- Rafael Ceneme 9898610
- muketa
- João Villaça 10724239
- Matheus Populim 10734710



<div align="center">
<h1>Nabocoin</h1>
<h2>O Blockchain-as-a-service mais simples que existe</h2>
</div>

<div align="center">
  <img src="ws/application/static/img/icon.png" width="300px" height="300px"/>
</div>
<div align="center">Ícones feitos por <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/br/" title="Flaticon">www.flaticon.com</a></div>
<br>
<div align="center">
>Blockchain PoW (Proof-of-Work) simples
</div>
<br>

Para executar a aplicação, é necessário ter o kafka server e o zookeeper rodando.
É necessário incluir o IP público da máquina no arquivo server.properties:
```bash
    > bin/zookeeper-server-start.sh config/zookeeper.properties
    > bin/kafka-server-start.sh config/server.properties
```

Para criar um ambiente virtual para testar o aplicativo, execute os comandos:

(Linux/Bash):
```bash
    ~$ python -m venv venv
    ~$ source venv/bin/activate
```
(Windows/Powershell):
```powershell
    > python -m venv venv
    > /venv/scripts/activate.ps1
```

Os requisitos devem ser instalados via pip:
```bash
    $ (venv) pip install -r requirements.txt
```




Vá para a pasta onde está o arquivo run.py e execute:
```bash
    > (venv) python run.py
```
Para evitar de ter de utilizar diversos terminais para executar todos os comandos, siga as seguintes instruções:
```bash
    > (venv) nohup python run.py &
```
O comando nohup no início permite redirecionar o output para um arquivo, evitando a poluição do terminal, e o operador & permite que o usuário dê um Enter e volte a ter controle do terminal.

Para interromper o programa, execute: 
```bash
    > (venv) ps aux | grep run.py
```

E mate o processo a partir de seu PID:
```bash
    > (venv) kill 123666
```

O nosso nó do Kafka padrão está no arquivo node.py na pasta kafkapython
Para executar 3 nós que interagem entre si através do kafka, execute:
```bash
    $ (venv) nohup python3 node1.py & nohup python3 node2.py & nohup python3 node3.py &
```

A cada ``` 10*(6 + random.randint(0,6)) ``` segundos, um destinatário e um remetemente são escolhidos aleatoriamente, enviando de 0 a 10 moedas para o outro. Cada usuário começa com 1000 moedas, e a quantidade total de cada usuário é atualizada através do Kafka Consumer.
Para ver as atualizações do Kafka, acesse a home do aplicativo ( http://andromeda.lasdpc.icmc.usp.br:8055/ ), ou então, utilize a API que retorna essas informações no formato JSON ( http://andromeda.lasdpc.icmc.usp.br:8055/jsondump ).
Se um producer mandar as mensagens para o tópico utilizado, o kafka receberá as informações, as distribuirá para outros nós, e quando atualizado, a página web mostrará as atualizações.
