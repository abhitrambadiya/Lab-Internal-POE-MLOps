pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = "1"
        APP_IMAGE = "mlops-hello-poe:latest"
    }

    stages {
        stage('Checkout Source') {
            steps {
                echo '=== Stage 1: Pulling code from GitHub repository ==='
                checkout scm
            }
        }

        stage('Environment & Tool Verification') {
            steps {
                echo '=== Stage 2: Verifying Tooling Environment ==='
                sh 'python3 --version || python --version'
                sh 'docker --version'
                sh 'git --version'
            }
        }

        stage('Pytest Automation') {
            steps {
                echo '=== Stage 3: Running Automated Test Cases ==='
                sh 'pytest tests/ -v'
            }
        }

        stage('Docker Build & Package') {
            steps {
                echo '=== Stage 4: Building Lightweight Alpine Docker Image ==='
                sh 'docker build -t ${APP_IMAGE} .'
            }
        }

        stage('Docker Dry Run Execution') {
            steps {
                echo '=== Stage 5: Container UAT Dry Run Execution ==='
                sh 'docker run --rm ${APP_IMAGE}'
            }
        }

        stage('Evidently Model Monitoring') {
            steps {
                echo '=== Stage 6: Running Evidently Data Drift & Performance Monitoring ==='
                sh 'python3 monitoring/monitor.py'
            }
        }
    }

    post {
        always {
            echo '=== MLOps CI/CD Pipeline Execution Completed ==='
        }
        success {
            echo 'UAT Dry Run Verification Status: SUCCESS'
        }
        failure {
            echo 'UAT Dry Run Verification Status: FAILED'
        }
    }
}
