from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/myprojects')
def login():
    return render_template("myprojects.html")


@auth.route('/mylinks')
def signup():
    return render_template("mylinks.html")

