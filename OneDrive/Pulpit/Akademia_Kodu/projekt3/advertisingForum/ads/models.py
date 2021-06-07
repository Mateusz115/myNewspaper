from django.db import models
from django.contrib.auth.models import User

class Advertisment(models.Model):
    company = models.CharField(max_length=300)
    address = models.CharField(max_length=400)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=14)
    desc = models.TextField()
    
    industries = [
        #('skrót który jest przechowywany w bazie danych', pelna nazwa widoczna do uzytkownika)
        ('','Choose industry'),
        ('re','Real state'),
        ('ht','Health'),
        ('at','Automotiv'),
        ('ft', 'Fitness'),
    ]
    industry = models.CharField(max_length=2,choices=industries, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #likes

    def __str__(self):
        return self.company
