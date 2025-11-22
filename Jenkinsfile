pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-app"
        CONTAINER_NAME = "flask-app-container"
        HOST_PORT = "5001"
        CONTAINER_PORT = "5000"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                docker build -t ${IMAGE_NAME}:latest .
                """
            }
        }

        stage('Stop & Remove Existing Container') {
            steps {
                sh """
                if [ \$(docker ps -aq -f name=${CONTAINER_NAME}) ]; then
                    docker stop ${CONTAINER_NAME}
                    docker rm ${CONTAINER_NAME}
                fi
                """
            }
        }

        stage('Run Docker Container') {
            steps {
                sh """
                docker run -d --name ${CONTAINER_NAME} -p ${HOST_PORT}:${CONTAINER_PORT} ${IMAGE_NAME}:latest
                """
            }
        }

        stage('Health Check') {
            steps {
                sh """
                echo "Waiting for Flask app to start..."
                sleep 5  # Wait for the app to initialize
                echo "Checking if app is running..."
                
                # Retry up to 5 times
                for i in {1..5}; do
                    curl -f http://localhost:${HOST_PORT} && break || sleep 2
                done
                """
            }
        }

        stage('Cleanup Old Images') {
            steps {
                sh """
                docker image prune -f
                """
            }
        }
    }

    post {
        success {
            echo "Pipeline succeeded. Flask app is running on port ${HOST_PORT}."
        }
        failure {
            echo "Pipeline failed. Check logs for errors."
        }
    }
}



