#!flask/bin/python
from application import app

#chama a aplicação
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=80)