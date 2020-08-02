pipeline {
    agent any
    stages {
        stage('Build and Test Docker Image') {
            steps {
                script {
                    app = docker.build("0cl0tiry/reserver-backend")
                    app.inside {
			sh 'nohup python server.py &'
                        sh 'curl localhost:5000'
                        sh 'nosetests'
                    }
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
                        sh " ssh -i $SSH_KEY -To StrictHostKeyChecking=no $USERNAME@$backend_ip \"docker pull 0cl0tiry/reserver-backend:${env.BUILD_NUMBER}\""
                        try {
                            sh " ssh -i $SSH_KEY -To StrictHostKeyChecking=no $USERNAME@$backend_ip \"docker stop reserver-backend\""
                            sh " ssh -i $SSH_KEY -To StrictHostKeyChecking=no $USERNAME@$backend_ip \"docker rm reserver-backend\""
                        } catch (err) {
                            echo: 'caught error: $err'
                        }
                        sh " ssh -i $SSH_KEY -To StrictHostKeyChecking=no $USERNAME@$backend_ip \"docker run --restart always --name reserver-backend -p 5000:5000 -d 0cl0tiry/reserver-backend:${env.BUILD_NUMBER}\""
                    }
                }
            }
        }
    }
}
