pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/avinash943/Hello-World.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t fibonacci-app .'
            }
        }

        stage('Run Fibonacci App') {
            steps {
                sh 'echo 10 | docker run -i fibonacci-app'
            }
        }
    }
}
