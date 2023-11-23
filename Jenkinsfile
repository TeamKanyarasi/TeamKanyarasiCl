pipeline{
    agent any

    environment{
        EC2_HOST = 'ubuntu@IP ADDRESS'
        REMOTE_DIR = '/home/ubuntu'
    }
    stages{
        stage('Git Checkout'){
            steps{
                echo 'Initiating Git checkout ...'
                git url: 'https://github.com/TeamKanyarasi/TeamKanyarasiCl.git', branch: 'main'
            }
        }
        stage('Build'){
            steps{
                echo 'Initiating the Build to install dependencies...'
                sh '''
                pip install requirements.txt
                '''
            }
        }
        stage('Test'){
            steps{
                echo 'Initiating the Unit Testing using pytest framework...'
                sh 'pytest'
                
            }
        }
        stage('Deploy'){
            when {
                expression { currentBuild.result == 'SUCCESS' }
            }
            steps{
                echo 'Deploying to staging environment...'
                sshagent(['GLOBAL_CRED_ID']){
                    sh '''
                    scp -o -r StrictHostKeyChecking=no ${WORKSPACE}/* ${EC2_HOST}:${REMOTE_DIR}
                    ssh ${EC2_HOST} "sudo mv /home/ubuntu/* /var/www/"
                    '''
                }
            }
        }

    }
    post {
    failure {
        emailext body: 'The build failed', to: 'charanyandrapu@gmail.com', subject: 'Failed Pipeline: ${currentBuild.fullDisplayName}'
    }
    success {
        emailext body: 'The build succeeded', to: 'charanyandrapu@gmail.com', subject: 'Successful Pipeline: ${currentBuild.fullDisplayName}'
    }
    }  
}