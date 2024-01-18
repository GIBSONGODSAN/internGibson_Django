from django.db import models

class Sport(models.Model):
    sport_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class User(models.Model):
    user_id = models.AutoField(primary_key=True)  
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=10)
    sports = models.ForeignKey(Sport, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username
    
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
