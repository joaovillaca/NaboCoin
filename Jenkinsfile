pipeline {
    
    agent any

    stages {
        
        stage('Spawn') {
            steps {
                sh 'git clone https://github.com/zerodois-bcc/NaboCoin'
            }
            post {
                success {
                    echo '======= Repositorio clonado ======='
                }
            }
        }
        
        stage('Build') {
            agent {
                docker {
                    image 'python:3.8.5'
                }
            }
            
            steps {
                sh 'python -m venv venv'
                sh 'pip install -r requirements.txt'
                sh 'export FLASK_APP=run'
                sh 'flask run'
            }
        }
    }
}
