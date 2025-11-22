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

        stage('Run Tests') {
            steps {
                sh """
                if [ -f test_app.py ]; then
                    echo "Running pytest..."
                    pytest test_app.py || exit 1
                else
                    echo "No tests found, skipping..."
                fi
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

        stage('Deploy to Minikube') {
            steps {
                sh """
                eval \$(minikube -p minikube docker-env)
                kubectl apply -f flask-deployment.yaml
                kubectl apply -f flask-service.yaml
                kubectl get pods
                """
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed! Sending email notification...'
            // Uncomment below if you have Jenkins Email Extension configured
            // mail to: 'your-email@example.com',
            //      subject: "Jenkins Pipeline Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            //      body: "Check Jenkins for details: ${env.BUILD_URL}"
        }
    }
}

