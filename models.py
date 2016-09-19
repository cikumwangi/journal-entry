import os
import sys
import time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import *

import datetime

Base = declarative_base()


class Journal(Base):
	"""docstring for ClassName"""
	__tablename__ = 'journal'
	id = Column(Integer, autoincrement=True, primary_key =True)
	created_at = Column(DateTime, default= func.now())
	name = Column(String(255), unique=True)

	def __repr__(self):
		return "id: {} , name: {} , created_at: {}".format(self.id,
            self.name, self.created_at)

	
		


engine = create_engine('sqlite:///./database.db')
Base.metadata.create_all(bind=engine)