pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/sundarjee7/flask-devops-app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t flask-app:1.0 .
                '''
            }
        }
        stage('Run Docker Container') {
            steps {
                // Stop & remove any existing container first to avoid port conflicts
                sh '''
                if [ $(docker ps -aq -f name=flask-app-container) ]; then
                    docker stop flask-app-container
                    docker rm flask-app-container
                fi
                docker run -d --name flask-app-container -p 5001:5000 flask-app:1.0
                '''
            }
        }
    }
}

