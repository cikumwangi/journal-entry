from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import *

import datetime

Base = declarative_base()


class Journal(Base):
	"""docstring for ClassName"""
	__tablename__ = 'journal'
	id = Column(Integer, autoincrement=True, primary_key =True)
	created_at = Column(DateTime, default=datetime.datetime.today)
	name = Column(String(255), unique=True)
    

	
		


engine = create_engine('sqlite:///./database.db')
Base.metadata.create_all(bind=engine)