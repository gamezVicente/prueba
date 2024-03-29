import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for, current_app)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
   print('Request for index page received')
   return render_template('index.html')


if __name__ == '__main__':
   app.run()
