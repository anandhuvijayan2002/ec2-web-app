from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from AWS EC2!</h1><p>This app is running on Ubuntu (Free Tier)</p>"

@app.route('/about')
def about():
    return "<h1>About Me</h1><p>My name is Anandhu. This is my first EC2 Project!</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
