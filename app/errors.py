from flask import render_template
from app import app, db


@app.errorhandler(404)
def not_found_error(error):
    return render_template("error_404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("error_500.html"), 500
