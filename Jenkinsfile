pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "flask-app:latest"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/YOUR_USERNAME/YOUR_REPO.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Run Docker Container') {
            steps {
                // Stop old container if running
                sh '''
                if [ "$(docker ps -aq -f name=flask-container)" ]; then
                    docker rm -f flask-container || true
                fi
                '''

                // Run new container
                sh "docker run -d -p 5000:5000 --name flask-container ${DOCKER_IMAGE}"
            }
        }
    }

    post {
        success {
            mail to: 'suraine36@gmail.com',
                 subject: "Jenkins Build Successful",
                 body: "Your Flask app has been built, tested, and deployed successfully."
        }
        failure {
            mail to: 'suraine36@gmail.com',
                 subject: "Jenkins Build Failed",
                 body: "The build has failed. Please check Jenkins console output."
        }
    }
}

