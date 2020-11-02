from django.db.models import *
from accounts.models import User


class Question(Model):
    title = CharField(max_length=300)
    desc = TextField()
    image = ImageField(upload_to='images/', blank=True)
    createDate = DateTimeField(auto_now_add=True)
    user = ForeignKey(User, on_delete=CASCADE)

    schools = [
        ('', 'Wybierz szkołę'),
        ('ps', 'Szkoła Podstawowa'),
        ('ms', 'Szkoła Średnia'),
        ('cl', 'Studia'),
    ]
    school = CharField(max_length=2, choices=schools,
                       default='')

    subjects = [
        ('', 'Wybierz przedmiot'),
        ('mat', 'Matematyka'),
        ('fiz', 'Fizyka'),
        ('inf', 'Informatyka'),
        ('pol', 'Język Polski'),
        ('ang', 'Język Angielski'),
        ('nmc', 'Język Niemiecki'),
        ('his', 'Historia'),
        ('bio', 'Biologia'),
        ('che', 'Chemia'),
        ('geo', 'Geografia'),
    ]
    subject = CharField(max_length=3, choices=subjects,
                        default='')

    def __str__(self):
        return self.title
