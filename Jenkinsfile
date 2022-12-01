pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Attakay78/BlackJackPythonGame.git']]])
            }
        }
        stage('Build') {
            steps {
                git branch: 'master', url: 'https://github.com/Attakay78/BlackJackPythonGame.git'
                sh 'python3 Game.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m unittest -v test_player.py'
            }
        }
    }
}
