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
                sh 'docker build -t flask-app:1.0 .'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 flask-app:1.0'
            }
        }
    }
}
