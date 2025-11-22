pipeline {
    agent any

    environment {
        APP_NAME = "flask-app"
        APP_PORT = "5001"
        IMAGE_TAG = "${APP_NAME}:${BUILD_NUMBER}"
        CONTAINER_NAME = "${APP_NAME}-container"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/sundarjee7/flask-devops-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                docker build -t ${IMAGE_TAG} .
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
                docker run -d --name ${CONTAINER_NAME} -p ${APP_PORT}:5000 ${IMAGE_TAG}
                """
            }
        }

        stage('Health Check') {
            steps {
                sh """
                echo "Checking if app is running..."
                curl -f http://localhost:${APP_PORT} || exit 1
                """
            }
        }

        stage('Cleanup Old Images') {
            steps {
                sh "docker image prune -f"
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully! App running at http://localhost:${APP_PORT}"
        }
        failure {
            echo "Pipeline failed. Check logs for errors."
        }
    }
}


