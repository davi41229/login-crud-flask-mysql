from flask import render_template, request, redirect, url_for


from app import app
from app.controllers import default



if __name__ == '__main__':
    app.run(debug=True)