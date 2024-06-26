pipeline {
    agent any

    environment {
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
                    if (!fileExists("${env.WORKSPACE}\\${env.VIRTUALENV}\\Scripts\\activate")) {
                        bat 'python -m venv venv'
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                bat 'venv\\Scripts\\activate && python run.py'
            }
        }
        stage('Stop Flask App') {
            steps {
                script {
                    // Find Flask app process ID using PowerShell
                    def flaskProcess = powershell(returnStdout: true, script: '''
                        Get-Process python | Where-Object { $_.MainWindowTitle -like "*cmd*" } | Select-Object -ExpandProperty Id
                    ''').trim()
                    if (flaskProcess) {
                        bat "taskkill /PID ${flaskProcess} /F"
                    }
                }
            }
        }
        stage('Post-Execution Cleanup') {
            steps {
                echo 'Pipeline execution complete.'
                // Optionally add commands to clean up or stop the Flask app if needed
            }
        }
    }
}
