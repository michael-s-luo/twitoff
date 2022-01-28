# user tables and tweets table

from flask_sqlalchemy import SQLAlchemy

# create DB object

DB = SQLAlchemy()  # opens connection & cursor

# Create table with schema with python class


class User(DB.Model):
    # two columns for users
    # ID column schema
    id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)
    # Username column schema
    username = DB.Column(DB.String, nullable=False)


class Tweet(DB.Model):
    # ID column schema
    id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)

    # Text column schema, inc emojis and other characters
    text = DB.Column(DB.Unicode(300), nullable=False)

    # user column schema
    user_id = DB.Column(
        DB.BigInteger, DB.ForeignKey("user.id"), nullable=False
    )

    # Set up relationship between tweets and users
    user = DB.relationship("User", backref=DB.backref("tweets"), lazy=True)
