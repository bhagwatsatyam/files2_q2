pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/bhagwatsatyam/files2_q2.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python test_app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t event-app .'
            }
        }

        stage('Run Container') {
            steps {
                bat '''
                docker stop event-container || exit 0
                docker rm event-container || exit 0
                docker run -d -p 3003:3003 --name event-container event-app
                '''
            }
        }
    }

    post {
        success {
            echo 'BUILD SUCCESS'
        }
        failure {
            echo 'BUILD FAILED'
        }
    }
}