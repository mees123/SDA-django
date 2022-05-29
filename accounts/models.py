from django.db.models import Model, OneToOneField, CASCADE, TextField, CharField
from django.contrib.auth.models import User


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    biography = TextField()

    GENDER_CHOICES = (
        ("M", 'Male'),
        ("F", 'Female')
    )
    gender = CharField(max_length=1, choices=GENDER_CHOICES)
