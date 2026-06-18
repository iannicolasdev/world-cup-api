from flask import Flask
from app.routes import bp

app = Flask(__name__)
app.json.sort_keys = False 
app.register_blueprint(bp)