pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }
    stages {
        stage('Clone') {
            steps {
                git branch: 'develop', credentialsId: 'github', url: 'https://github.com/tech-2k/L.Oreal-demo.git'
            }
        }

        stage('Build Docker Image') {         
            steps{                
                sh 'docker build -t khraiteka/L.Oreal:$BUILD_NUMBER .'           
                echo 'Build Image Completed'                
            }           
        }

        stage('Login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('Push') {
            steps {
                sh 'docker push khraiteka/L.Oreal:$BUILD_NUMBER'
                echo 'Push Image Completed' 
            }
        }
    }
    post {
        success {
            slackSend color: '#36a64f', message: "Deployment of myapp to production succeeded!"
        }
        failure {
            slackSend color: '#ff0000', message: "Deployment of myapp to production failed!"
        }
  }
}