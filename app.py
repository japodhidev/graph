from flask import Flask
app = Flask(__name__)

@app.route('/')
def hey_there():
	return 'Hey there.'