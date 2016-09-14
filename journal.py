import os
import click
from colorama import init, Back, Fore, Style
from pyfiglet import Figlet

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import select
from models import Base,Journal


engine = create_engine('sqlite:///./database.db')
Base.metadata.bind = engine

# associate with the custom Session class
DBSession = sessionmaker(bind=engine)
session = DBSession()



def create_entry(name):
	"""
	Add a new entry
	"""
	entry = Journal(name=name)
	session.add(entry)
	session.commit()
	print "successfully added"
