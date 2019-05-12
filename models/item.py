from db import db

class ItemModel(db.Model):
    ''' ItemModel is an object containing:
        name, and price.
    '''
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name':self.name, 'price':self.price}

    @classmethod
    def find_by_name(cls, name):

        ''' The line:
            return ItemModel.query.filter_by(name=name).first()
        performs:
        SELECT * FROM items WHERE name=name LIMIT 1
        Because its a class nethod we can use cls
        '''
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        ''' Insert the current object to the database. Can do an
            update and insert. The session is a collection of obejects
            that can be written to the database'''
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        ''' delete an itemModel from the database. This will do:
            "DELETE FROM items WHERE name=?"
        '''
        db.session.delete(self)
        db.session.commit()

        return {"message":"Item '{}' updated".format(item['name'])}
