pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-app:latest"
        CONTAINER_NAME = "flask-app-container"
        MINIKUBE_CONTEXT = "minikube"
        EMAIL_RECIPIENT = "developer@example.com"  // replace with your email
    }

    stages {
        stage('Checkout SCM') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/sundarjee7/flask-devops-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh '''
                        echo "Running pytest inside Docker container..."
                        docker run --rm -v $PWD:/app -w /app ${IMAGE_NAME} pytest test_app.py
                    '''
                }
            }
        }

        stage('Stop & Remove Existing Container') {
            steps {
                script {
                    sh '''
                        if [ $(docker ps -a -q -f name=${CONTAINER_NAME}) ]; then
                            echo "Stopping and removing existing container..."
                            docker stop ${CONTAINER_NAME}
                            docker rm ${CONTAINER_NAME}
                        else
                            echo "No existing container found"
                        fi
                    '''
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh "docker run -d --name ${CONTAINER_NAME} -p 5001:5000 ${IMAGE_NAME}"
                }
            }
        }

        stage('Deploy to Minikube') {
            steps {
                script {
                    sh '''
                        echo "Deploying to Minikube..."
                        kubectl apply -f flask-deployment.yaml
                        kubectl apply -f flask-service.yaml
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed! Sending email notification...'
            mail to: "${EMAIL_RECIPIENT}",
                 subject: "Jenkins Pipeline Failed: ${JOB_NAME}",
                 body: "The Jenkins pipeline for ${JOB_NAME} failed. Please check the console output."
        }
    }
}

