import json
from sqlalchemy.orm import DeclarativeMeta

from app import db


def save_entity(entity):
    db.session.add(entity)
    db.session.commit()


class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        import datetime
        if isinstance(obj.__class__, DeclarativeMeta):
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    if isinstance(data, datetime.date):
                        fields[field] = data.strftime("%m/%d/%Y")
                    else:
                        fields[field] = None
            return fields

        return json.JSONEncoder.default(self, obj)


class Spolka(db.Model):
    __tablename__ = 'spolka'
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(200), unique=True)
    waluta = db.Column(db.String(200))
    kursy = db.relationship('Kursy', backref='sp')

    def __init__(self, nazwa, waluta, ):
        self.nazwa = nazwa
        self.waluta = waluta


class Kursy(db.Model):
    __tablename__ = 'kursy'
    id = db.Column(db.Integer, primary_key=True)
    data_dodania = db.Column(db.Date)
    kurs_otw = db.Column(db.Float)
    kurs_max = db.Column(db.Float)
    kurs_min = db.Column(db.Float)
    kurs_zamkn = db.Column(db.Float)
    liczba_trans = db.Column(db.Float)
    obrot = db.Column(db.Float)
    sp_id = db.Column(db.Integer, db.ForeignKey('spolka.id'))

    def __init__(self, data_dodania, kurs_otw, kurs_max, kurs_min, kurs_zamkn, liczba_trans, obrot, sp_id):
        self.data_dodania = data_dodania
        self.kurs_otw = kurs_otw
        self.kurs_max = kurs_max
        self.kurs_min = kurs_min
        self.kurs_zamkn = kurs_zamkn
        self.liczba_trans = liczba_trans
        self.obrot = obrot
        self.sp_id = sp_id


#db.drop_all()
db.create_all()
