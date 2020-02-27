pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    app = docker.build("n0nce/tennis-server")
                    app.inside {
                        sh 'echo $(curl localhost:5000)'
                    }
                }
            }
        }
        stage('Test Docker Image') {
            steps {
                script {
                        sh "nosetests"
                    }
                }
            }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker_hub_login') {
                        app.push("${env.BUILD_NUMBER}")
                        app.push("latest")
                    }
                }
            }
        }
        stage('DeployToProduction') {
            steps {
                input 'Deploy to Production?'
                milestone(1)
                withCredentials([sshUserPrivateKey(credentialsId: 'backend_ssh', usernameVariable: 'USERNAME', keyFileVariable: 'SSH_KEY')]) {
                    script {
                        sh " ssh -i $SSH_KEY -To StrictHostKeyChecking=no $USERNAME@$backend_ip \"docker pull n0nce/tennis-server:${env.BUILD_NUMBER}\""
                        try {
                            sh " ssh -i $SSH_KEY -To StrictHostKeyChecking=no $USERNAME@$backend_ip \"docker stop tennis-server\""
                            sh " ssh -i $SSH_KEY -To StrictHostKeyChecking=no $USERNAME@$backend_ip \"docker rm tennis-server\""
                        } catch (err) {
                            echo: 'caught error: $err'
                        }
                        sh " ssh -i $SSH_KEY -To StrictHostKeyChecking=no $USERNAME@$backend_ip \"docker run --restart always --name tennis-server -p 5000:5000 -d n0nce/tennis-server:${env.BUILD_NUMBER}\""
                    }
                }
            }
        }
    }
}
