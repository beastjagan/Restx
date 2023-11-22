from . import db, orm, fields

class User(db.Entity):
    _table_ = 'users'
    id = orm.PrimaryKey(int,auto=True)
    first_name = orm.Required(str, 40)
    second_name = orm.Required(str, 40)
    age = orm.Required(int)
    
    

db.generate_mapping(create_tables=True)


user_schema = {
    "id": fields.Integer(),
    "first_name": fields.String(),
    "second_name": fields.String(),
    "age": fields.Integer()
}