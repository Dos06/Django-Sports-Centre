from django.db import models

# Create your models here.

# SUBSCRIPTION_TYPE_CHOICES = (
#     ('gym', 'Gym'),
#     ('cross_fit', 'Cross Fit'),
#     ('volleyball', 'Volleyball'),
#     ('box', 'Boxing')
# )


class User(models.Model):
    SUBSCRIPTION_TYPE_CHOICES = (
        ('gym', 'Gym'),
        ('crossfit', 'CrossFit'),
        ('volleyball', 'Volleyball'),
        ('box', 'Boxing')
    )
    GENDER_TYPE_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    member_id = models.AutoField(primary_key=True)
    first_name = models.CharField(('Name'), max_length=50)
    last_name = models.CharField(('Surname'), max_length=50)
    gender = models.CharField(('Gender'), max_length=10, choices=GENDER_TYPE_CHOICES)
    login = models.CharField(('Login'), max_length=50, unique=True)
    password = models.CharField(('Password'), max_length=50)
    age = models.IntegerField(('Age'))
    activity = models.CharField(('Activity'), max_length=50, choices=SUBSCRIPTION_TYPE_CHOICES)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.gender + ' ' + self.activity
    # TO-DO ADD AGE (don't know why there is no column 'Age')


# example how to create a record in DB (for Dos, Aldy ne trogay)
# user = User(first_name='Lyudmila',
#             last_name='Issayeva',
#             gender='Female',
#             login='lyuda',
#             password='lyudmilapass',
#             age='26',
#             activity='volleyball')
# user.save()
# user.login = 'lyudmila'
# user.save
# User.objects.all()          # show all class members
# User.objects.filter(activity='volleyball')
