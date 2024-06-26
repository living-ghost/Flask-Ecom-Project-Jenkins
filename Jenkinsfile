pipeline {
    agent any

    environment {
        // Define any environment variables here
        VIRTUALENV = 'venv'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/living-ghost/Flask-Ecommerce-Project-Beginner-Friendly-.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                script {
                    // Check if virtual environment exists, if not create one
                    if (!fileExists("${env.WORKSPACE}/${env.VIRTUALENV}/bin/activate")) {
                        sh 'python3 -m venv venv'
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                sh '. venv/bin/activate && python app.py'
            }
        }
    }
}
