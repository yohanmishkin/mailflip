from app import create_app
from flask_script import Manager

app = create_app()
manager = Manager(app)

@manager.command
def run():
	app.run()

if __name__ == "__main__":
	manager.run()