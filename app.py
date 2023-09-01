# -*- coding: utf-8 -*-
from flask import Flask, render_template, Blueprint, jsonify

app = Flask(__name__)
app_blueprint = Blueprint('default', __name__, template_folder='templates', static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')


@app_blueprint.route('/hello')
def default_route():
    """Confirm that the application is working."""
    return jsonify({'hello': 'from template api auto-deployed!'}), 200
