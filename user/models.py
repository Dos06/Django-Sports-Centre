from django.db import models

# Create your models here.

SUBSCRIPTION_TYPE_CHOICES = (
    ('gym', 'Gym'),
    ('cross_fit', 'Cross Fit'),
    ('volleyball', 'Volleyball'),
    ('box', 'Boxing')
)


class User(models.Model):
    member_id = models.AutoField(primary_key=True)
    first_name = models.CharField(('Name'), max_length=50)
    last_name = models.CharField(('Surname'), max_length=50)
    gender = models.CharField(('Gender'), max_length=10)
    login = models.CharField(('Login'), max_length=50, unique=True)
    password = models.CharField(('Password'), max_length=50)
    activity = models.CharField(('Activity'), max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
