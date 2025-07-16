pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t fibonacci-app .'
            }
        }

        stage('Run Fibonacci') {
            steps {
                sh 'echo 10 | docker run -i fibonacci-app'
            }
        }
    }
}
