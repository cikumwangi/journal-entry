import os
import click
from colorama import init, Back, Fore, Style
from sqlalchemy import func

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import select
from models import Base, Journal
from datetime import datetime


engine = create_engine('sqlite:///./database.db')
Base.metadata.bind = engine

# associate with the custom Session class
DBSession = sessionmaker(bind=engine)
session = DBSession()


@click.group()
def cli():
    pass
    create_entry()   



@click.command()
@click.option('--name', prompt='journal entry')
def create_entry(name):
    """
    Add a new entry
    """
    entry = Journal(name=name)
    session.add(entry)
    session.commit()
    print "successfully added"
    print "\t id:{}, \n\t name: \n\t\t{} ".format(id,
                                         name)

@click.command()
@click.option('--name', prompt='listing journals')
def list_all(name):
	"""
	Lists all Entries
	"""
	print("ID\t\t\tDescription\t\t\tDate\n")	
	for instance in session.query(Journal).order_by(Journal.id):
		
		print str(instance.id).ljust(15), instance.name.ljust(20)


@click.command()
@click.option('--name', prompt='listing name column')	
def search(name, word):
	"""
	Search entry by name
	"""
	splitname = name.split()

	q = session.query(Journal.name.label('splitname')).all()
	for row in range(len(q.splitname)):
		if splitname[row] == word:
			return ''.join(splitname)


	# for elem  in range(len(q)):
 #        	print(result.name)

	# q = session.query(Journal.name.label('name_label')).all()
	
	# for row in q.name_label:
	# 	if result in row:
	# 		print (q.name_label)
	# 	else:
	# 		return "Not found"
		

		# print (row.name_label)
	# for row in session.query(Journal).filter(Journal.name== 'name').all():
	# 	print (row.name)


	# result = '
	# q = session.query(Journal).filter_by(name=name)
	# q = session.query(Journal).filter(Journal.name=name)).all()
	# for q in name:
	# 		print "result found: {}".format(name)

		# if name in q:
		# 	return q
		# else:
		# 	return "not found"

	# result_name = {name: i for i in q}
	# result = [result_name[n] for n in name]




if __name__ == '__main__':
	search()
