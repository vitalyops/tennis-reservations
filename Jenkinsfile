pipeline {
    agent any
    stages {
        stage('Build and Test Docker Image') {
            steps {
                script {
                    app = docker.build("n0nce/tennis-server")
                    app.inside {
                        sh 'echo $(curl localhost:5000)'
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
                        sh "sh ssh -To -i $SSH_KEY StrictHostKeyChecking=no $USERNAME@backend_ip \"docker pull n0nce/tennis-server:${env.BUILD_NUMBER}\""
                        try {
                            sh "sh ssh -To -i $SSH_KEY StrictHostKeyChecking=no $USERNAME@backend_ip \"docker stop tennis-server\""
                            sh "sh ssh -To -i $SSH_KEY StrictHostKeyChecking=no $USERNAME@backend_ip \"docker rm tennis-server\""
                        } catch (err) {
                            echo: 'caught error: $err'
                        }
                        sh "sh ssh -To -i $SSH_KEY StrictHostKeyChecking=no $USERNAME@backend_ip \"docker run --restart always --name tennis-server -p 5000:5000 -d n0nce/tennis-server:${env.BUILD_NUMBER}\""
                    }
                }
            }
        }
    }
}
