from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "Hello from 2mdks171 Elastic Beanstalk CI-CD"

if __name__ == "__main__":
    application.run()
