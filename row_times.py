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
    },
    {
        'distance': 2000
        'time': 8:02.2
        'date': 12/12/16
    },
    {
        'distance': 2000
        'time': 7:59.9
        'date': 14/12/16
    },
    {
        'distance': 2000
        'time': 7:45.4
        'date': 30/12/16
    },
    {
        'distance': 2000
        'time': 7:23.7
        'date': 31/12/16
    },
    {
        'distance': 2000
        'time': 7:28.1
        'date': 2/01/17
    },
    {
        'distance': 2000
        'time': 7:45.8
        'date': 16/01/17
    },
    {
        'distance': 2000
        'time': 7:24.4
        'date': 18/01/17
    },
    {
        'distance': 2000
        'time': 10:00.3
        'date': 19/01/17
    },
    {
        'distance': 500
        'time': 1:38.3
        'date': 19/01/17
    },
    {
        'distance': 2000
        'time': 10:00.1
        'date': 19/01/17
    },
    {
        'distance': 2000
        'time': 9:00.2
        'date': 25/01/17
    },
    {
        'distance': 2000
        'time': 8.00.2
        'date': 30/01/17
    },
    {
        'distance': 1000
        'time': 4:18
        'date': 19/12/17
    },
    {
        'distance': 2000
        'time': 8:42.2
        'date': 22/12/17
    },
    {
        'distance': 2000
        'time': 7:55.0
        'date': 26/12/17
    },
    {
        'distance': 2000
        'time': 7:42.1
        'date': 27/12/17
    },
    {
        'distance': 2000
        'time': 7:58.5
        'date': 28/12/17
    }
]

if __name__ == '__main__':
    db.connect()
    db.create_tables([RowTime], safe=True)
