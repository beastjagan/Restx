from pony import *
from pony import orm
from pony.orm import select
from flask_restx import fields


db = orm.Database()

db.bind(provider='sqlite', filename='pony_test.db', create_db=True)


session = orm.db_session







