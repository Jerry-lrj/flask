from flask import Blueprint

web = Blueprint('web',__name__)

from app.controller import massage,login
