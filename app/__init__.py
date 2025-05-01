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
    
    @app.route('/wishes')
    def wishes():
        return render_template('wishes.html')

    @app.route('/plans')
    def plans():
        return render_template('plans.html')

    @app.route('/ps')
    def ps():
        return render_template('ps.html')
    return app