from flask import Flask, render_template
from .models import DB, User, Tweet


def create_app():

    app = Flask(__name__)

    # configuration variables
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # connect app with DB
    DB.init_app(app)

    @app.route("/")
    def home():
        # query for existing users
        users = User.query.all()

        return render_template("base.html", title="Home", users=users)

    @app.route("/populate")
    def populate():
        # Reset database first
        DB.drop_all()

        # Recreate tables
        DB.create_all()

        # Make 2 new users & 2 tweets
        michael = User(id=1, username="michaelluo")
        janet = User(id=2, username="janlee")

        tweet1 = Tweet(id=1, text="michael's tweet", user=michael)
        tweet2 = Tweet(id=2, text="janet's tweet", user=janet)

        # insert
        DB.session.add(michael)
        DB.session.add(janet)
        DB.session.add(tweet1)
        DB.session.add(tweet2)

        # commit changes
        DB.session.commit()

        return render_template("base.html", title="Populate")

    @app.route("/reset")
    def reset():
        """Drop all tables"""
        DB.drop_all()

        # Recreate tables
        DB.create_all()

        return render_template("base.html", title="Reset Database")

    return app
