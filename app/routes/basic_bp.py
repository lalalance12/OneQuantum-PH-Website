from flask import render_template, redirect, request, url_for, flash
from flask import Blueprint

basic_bp = Blueprint('pages', __name__)

@basic_bp.route('/about-us')
def about_us():
    return render_template('about_us.html')

@basic_bp.route('/services')
def services():
    return render_template('services.html') 

@basic_bp.route('/contacts')
def contacts():
    return render_template('contacts.html') 

