pipeline {
    agent any

    stages {
        stage('Pull') {
            steps {
                sh 'docker-compose pull'
            }
        }
        stage('Build') {
            steps {
                sh 'cp ../../saleor_secrets/secrets.py ./saleor'
                sh 'docker-compose build'
            }
        }
        stage('Prepare') {
            steps {
                sh 'docker-compose run --rm web python3 manage.py makemigrations'
                sh 'docker-compose run --rm web python3 manage.py migrate'
                sh 'docker-compose run --rm web python3 manage.py collectstatic'
            }
        }
        stage('Test') {
            steps {
                sh 'docker-compose run --rm web python3 manage.py test'
            }
        }
        stage('Deploy-SIT check') {
            steps {
                input "Would you ike to deploy to the test environment"
            }
        }
        stage('Deploy-SIT') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}

