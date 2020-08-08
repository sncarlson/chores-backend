# TODO Use of correct data types for fields
# TODO Use of primary and optional foreign key ids

# TODO Does not use raw SQL or only where there are not SQLAlchemy equivalent expressions
# TODO Correctly formats SQLAlchemy to define models
# TODO Creates methods to serialize model data and helper methods to simplify API behavior
#  such as insert, update and delete.

from chores.database.database import db


class Chore(db.Model):
    __tablename__ = 'Chores'

    id = db.Column(db.Integer, primary_key=True)
