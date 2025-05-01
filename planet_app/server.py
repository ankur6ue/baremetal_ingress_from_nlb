from flask import Flask, render_template, jsonify
import random

def page_not_found(e):
  return jsonify(server_name="flask_server", error=str(e)), 404


app = Flask(__name__)
app.register_error_handler(404, page_not_found)


@app.route('/')
def hello_world():
    # create a random number and append to the string
    num = random.randint(0, 100)
    return f'Hello, World! {num}\n'


@app.route('/mars')
def hello_mars():
    num = random.randint(0, 100)
    return f'Hello, Martians! {num}\n'


@app.route('/saturn/titan')
def hello_titan():
    num = random.randint(0, 100)
    return f'Hello, Titans of Saturn! {num}\n'


@app.route('/saturn/enceladus')
def hello_enceladus():
    num = random.randint(0, 100)
    return f'Hello, Enceladuns of Saturn! {num}\n'


if __name__ == '__main__':
    # host must be 0.0.0.0, otherwise won't work from inside docker container
    app.run(host='0.0.0.0', debug=True, use_reloader=False, port=5000)