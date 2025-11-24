pipeline {
  agent any

  environment {
    DOCKER_IMAGE = "flask-assessment:latest"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Install & Test') {
      steps {
        echo "Installing dependencies and running tests"
        sh '''
          python3 -m venv .venv
          . .venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
          pytest -q || { echo "Tests failed"; exit 1; }
        '''
      }
    }

    stage('Build Docker Image') {
      steps {
        echo "Building Docker Image: ${DOCKER_IMAGE}"
        sh '''
          docker build -t ${DOCKER_IMAGE} .
        '''
      }
    }

    stage('Run Container (smoke)') {
      steps {
        echo "Run app container for sanity check"
        sh '''
          docker rm -f flask-assessment-run || true
          docker run -d --name flask-assessment-run -p 5000:5000 ${DOCKER_IMAGE}
          sleep 3
          # basic healthcheck
          if ! curl --fail http://localhost:5000/ >/dev/null 2>&1; then
            docker logs flask-assessment-run || true
            exit 1
          fi
        '''
      }
    }

    stage('Archive & Cleanup') {
      steps {
        archiveArtifacts artifacts: '**/*.py, Dockerfile, Jenkinsfile, requirements.txt, README.md', fingerprint: true
        sh 'docker rm -f flask-assessment-run || true'
      }
    }
  }

  post {
    success {
      echo "Pipeline succeeded"
      // place for email/slack notification script (use credentials and notify)
    }
    failure {
      echo "Pipeline failed"
      // place for email/slack on failure
    }
  }
}

