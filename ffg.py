import Manager

app = Flask(__name__)
# configure your app

manager = Manager(app)

if __name__ == "__main__":
    manager.run()