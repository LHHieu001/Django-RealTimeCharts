from datetime import date
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class voter(models.Model):
    
    class candi(models.TextChoices):
        JOE_BIDEN = 'JOE', 'Joe Biden'
        KAMALA_HARRIS = 'HARRIS', 'Kamala Harris'
        BARACK_OBAMA = 'OBAMA', 'Barack Obama'
        DONALD_TRUMP = 'TRUMP', 'Donald Trump'
        MIKE_PENCE = 'MIKE', 'Mike Pence'
        NIKKI_HALLEY = 'HALLEY', 'Nikki Halley'
        KENNEDY_JR = 'KENNEDY', 'Robert F. Kennedy Jr'
        CORNEL_WEST = 'WEST', 'Cornel West'
        CHASE_OLIVER = 'OLIVER', 'Chase Oliver'
        NO_VOTE = 'NO VOTE', 'No'
        
        
            
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.CharField(max_length=100, choices=candi.choices, default=candi.NO_VOTE)
    date = models.DateField(default=date.today)
    
    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.date = date.today()
    #     super().save(*args, **kwargs)
    
    def __str__(self):
        return self.user.username
    
class userInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(default=None)
    dob = models.DateField(default=None)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=50)
    social = models.CharField(max_length=15)
    