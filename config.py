from flask import Flask
app = Flask ( __name__ )
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']
ABOUT = "Bienvenue sur la page à propos de Flask !"
CONTACT = "voici mon email: etienne.audor@etu.univ-orleans.fr"
TITLE = "R3.01 Dev Web avec Flask"

import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'monApp.db')