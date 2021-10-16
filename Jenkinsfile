pipeline { 

    //connect to the dockerhub enviroment by the dockerhub_id credentials
    environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub_id')
	}

    agent any 
    stages { 
        
        //first stage: cloning the project form github repo
        stage('git clone') { 
            steps { 
                git 'https://github.com/samahAbbas11/Docker_Final_Task.git' 
            }
        } 
        
        //second stage: build an image by docker 
        stage('Build image') { 
            steps { 
               
                sh 'docker build -t docker_final .'
                
            } 
        }
        
        //third stage: login to dockerhub in order to push the image
        //by username and password saved in jenkins global credintials 
        stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

        //last stage: Push the image to dockerhub repositorey 
		stage('Push') {

			steps {
			    sh' docker tag docker_final samahabbas11/docker_final'
				sh ' docker push samahabbas11/docker_final'
			}
		}
 
    }

}


