pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "flask-app:latest"
    }

    options {
        skipDefaultCheckout()
    }

    stages {

        stage('Checkout') {
            steps {
                git url: 'https://github.com/sundarjee7/flask-devops-app.git', branch: 'main'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    docker build -t flask-app-test .
                    docker run --rm flask-app-test pytest tests/
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                    if [ "$(docker ps -aq -f name=flask-container)" ]; then
                        echo "Old container found. Removing..."
                        docker rm -f flask-container || true
                    fi
                '''

                sh "docker run -d -p 5000:5000 --name flask-container ${DOCKER_IMAGE}"
            }
        }
    }

    post {
        always {
            echo "Cleaning up unused Docker resources..."
            sh 'docker system prune -f'
        }
    }
}

