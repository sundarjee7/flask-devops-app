pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-app:latest"
        CONTAINER_NAME = "flask-app-container"
        EMAIL_RECIPIENT = "rsundarjee2@gmail.com"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/sundarjee7/flask-devops-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Run Pytest inside Docker') {
            steps {
                sh '''
                    echo "Running tests inside Docker container..."
                    docker run --rm -v $PWD:/app -w /app ${IMAGE_NAME} pytest test_app.py
                '''
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                    if [ $(docker ps -aq -f name=${CONTAINER_NAME}) ]; then
                        docker stop ${CONTAINER_NAME} || true
                        docker rm ${CONTAINER_NAME} || true
                    fi
                '''
            }
        }

        stage('Run New Container') {
            steps {
                sh "docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}"
            }
        }
    }

    post {
        failure {
            mail to: "${EMAIL_RECIPIENT}",
                 subject: "❌ Jenkins Pipeline Failed",
                 body: "Your Flask CI/CD pipeline failed. Please check Jenkins logs."
        }
        success {
            echo "✔ Pipeline succeeded!"
        }
    }
}

