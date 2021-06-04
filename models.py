from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import not_

db = SQLAlchemy()
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
class VisitingTime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(15), unique=True, nullable=False)
    M1 = db.Column(db.Integer)
    M2 = db.Column(db.Integer)
    M3 = db.Column(db.Integer)
    M4 = db.Column(db.Integer)
    M5 = db.Column(db.Integer)
    M6 = db.Column(db.Integer)
    M7 = db.Column(db.Integer)
    M8 = db.Column(db.Integer)
    M9 = db.Column(db.Integer)
    M10 = db.Column(db.Integer)
    A1 = db.Column(db.Integer)
    A2 = db.Column(db.Integer)
    A3 = db.Column(db.Integer)
    A4 = db.Column(db.Integer)
    A5 = db.Column(db.Integer)
    A6 = db.Column(db.Integer)
    A7 = db.Column(db.Integer)
    A8 = db.Column(db.Integer)
    A9 = db.Column(db.Integer)
    A10 = db.Column(db.Integer)
    N1 = db.Column(db.Integer)
    N2 = db.Column(db.Integer)
    N3 = db.Column(db.Integer)
    N4 = db.Column(db.Integer)
    N5 = db.Column(db.Integer)
    N6 = db.Column(db.Integer)
    N7 = db.Column(db.Integer)
    N8 = db.Column(db.Integer)
    N9 = db.Column(db.Integer)
    N10 = db.Column(db.Integer)

    @classmethod
    def calc(class_, day, time, number, current):
        section = "M" if time >= 9 and time < 12 else "A" if time >= 13 and time < 17 else \
                "N" if time >= 18 and time < 21 else ""
        if not section: return "非看診時間"

        if day.startswith("Sat") or day.startswith("Sun"):
            data = db.session.query(class_).filter(VisitingTime.date.startswith("S")).all()
        else:
            data = db.session.query(class_).filter(not_(VisitingTime.date.startswith("S"))).all()
        dict = [vars(u) for u in data]

        dict_processed = [sorted([[k, v] for k,v in i.items() if k.startswith(section)], \
                            key = lambda a: int(a[0][1:])) for i in dict]

        data_selected = [[i.pop(1) for i in elem] for elem in dict_processed]
        
        waiting_time = sum([sum(i[current-1:number-1]) for i in data_selected])/len(data_selected)
        return waiting_time