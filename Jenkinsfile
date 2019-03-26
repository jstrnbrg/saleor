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
        stage('Makemigrations') {
            steps {
                sh 'docker-compose run --rm web python3 manage.py makemigrations'
            }
        }
        stage('Migrate') {
            steps {
                sh 'docker-compose run --rm web python3 manage.py migrate'
            }
        }
        stage('Collectstatic') {
            steps {
                sh 'docker-compose run --rm web python3 manage.py collectstatic --no-input'
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

