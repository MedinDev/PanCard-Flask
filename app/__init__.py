from flask import Flask

app = Flask(__name__)

# Set a default value for the ENV key
app.config.setdefault("ENV", "development")

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "development":
    app.config.from_object("config.DevelopmentConfig")
else:
    app.config.from_object("config.TestingConfig")

from app import views