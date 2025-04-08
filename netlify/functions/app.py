from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def handler():
    return jsonify(message="Hello from Flask Backend!")

# This makes the function work with Netlify
def handler(event, context):
    from flask_lambda import FlaskLambda
    flask_lambda = FlaskLambda(app)
    return flask_lambda(event, context)
  
