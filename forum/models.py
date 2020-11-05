from django.db.models import *
from accounts.models import User
from datetime import datetime,timezone
from forumSzkolne.settings import TIME_ZONE


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

    likes = ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def display_time(self):
        mytimezone = timezone.utc
        now = datetime.now(mytimezone)
        if self.createDate.date() == now.date():
            if self.createDate.hour == now.hour:
                return str(now.minute - self.createDate.minute)+" min. temu"
            else:
                return str(now.hour - self.createDate.hour)+" godz. temu"
        else:
            diff = (now - self.createDate).days
            if diff == 1:
                return str(diff)+" dzień temu"
            else:
                return str(diff)+" dni temu"
