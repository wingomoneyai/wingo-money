# Flask app routing
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home(): return 'Welcome to WinGoAi'