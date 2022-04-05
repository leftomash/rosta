from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from dotenv import load_dotenv
import os

if os.path.exists('.env'):
    load_dotenv()
    
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=os.environ.get('deploy_mode') == 'development')