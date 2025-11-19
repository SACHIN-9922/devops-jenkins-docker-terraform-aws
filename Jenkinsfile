pipeline {
    agent any

    environment {
        APP_NAME = "devops-demo-app"
        APP_PORT = "5000"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('app') {
                    sh '''
                        echo "Building Docker image..."
                        docker build -t ${APP_NAME}:${BUILD_NUMBER} .
                    '''
                }
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                    echo "Stopping old container (if exists)..."
                    docker stop ${APP_NAME} || true
                    docker rm ${APP_NAME} || true

                    echo "Starting new container..."
                    docker run -d --name ${APP_NAME} -p ${APP_PORT}:${APP_PORT} ${APP_NAME}:${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        success {
            echo "Deployment successful! Visit http://<EC2_PUBLIC_IP>:${APP_PORT}"
        }
        failure {
            echo "Build or deployment failed."
        }
    }
}
