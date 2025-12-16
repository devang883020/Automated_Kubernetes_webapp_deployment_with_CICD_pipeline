from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Jenkins CI/CD on EKS! with webhook gitlab and it is my first project and if there is any change please tell me "

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
