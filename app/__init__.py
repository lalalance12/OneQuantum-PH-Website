from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from config import SECRET_KEY 


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY

    @app.errorhandler(404)  # if a page is not found, return 404
    def page_not_found(e):
        return render_template('404.html'), 404
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    from app.routes.basic_bp import basic_bp

    app.register_blueprint(basic_bp, url_prefix='/')

    return app
