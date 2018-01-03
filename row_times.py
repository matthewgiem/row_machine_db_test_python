from peewee import *

db = SqlightDatabase('row_times.db')

class RowTime(Model):
    distance = IntegerField(default=0)
    time = IntegerField(default=0)
    date = IntegerField(default=0)

    class Meta:
        database = db

row_times = [
    {
    'distance': 5000
    'time': 23:15.6 # need to be converted
    'date':  2/01/18 # need to be converted
    }
]

if __name__ == '__main__':
    db.connect()
    db.create_tables([RowTime], safe=True)
