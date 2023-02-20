#from .weather_forms import
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
#from travelerApp.models import CharacterTbl, GameTbl, PlayerCharacterTbl, UserInfoTbl
#from .weather_funcs import 
from travelerApp import db
from wtforms.validators import ValidationError
from uuid import uuid4
from . import weather