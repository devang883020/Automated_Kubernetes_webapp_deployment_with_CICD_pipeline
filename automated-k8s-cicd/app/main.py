from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Jenkins CI/CD on EKS! with webhook github and CI with github action!! and wish me luck!!!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
