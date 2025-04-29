from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('config.Config')

    # Define routes
    @app.route("/")
    def home():
        return render_template("base.html")

    @app.route("/story")
    def story():
        return render_template("story.html")

    return app