from flask import Flask

from config import Config
from models import db
from routes import main_bp, users_bp, prefs_bp
from scheduler import scheduler
from cult_helper import cult_class_booker_for_all_users


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    db.init_app(app)

    scheduler.init_app(app)
    scheduler.start()

    scheduler.add_job(
        id="cult_class_booker",
        func=cult_class_booker_for_all_users,
        trigger="interval",
        seconds=10,
    )

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(prefs_bp, url_prefix="/preferences")

    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
