from django.db import models
<<<<<<< HEAD

class Team(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name} - {self.department}"

class User(models.Model):
    username = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='users')
    
    def __str__(self):
        return self.username

=======
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    # Add any additional fields here
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        swappable = 'AUTH_USER_MODEL'
>>>>>>> 094fb77 (DATA BASE ADDED FOR DATA)
class Department(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

<<<<<<< HEAD
=======
class Team(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} ({self.department.name})"

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    
    def __str__(self):
        return f"{self.name} - {self.team.name}"

>>>>>>> 094fb77 (DATA BASE ADDED FOR DATA)
class Session(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
<<<<<<< HEAD
        return self.name
=======
        return f"{self.name} - {self.date}"
>>>>>>> 094fb77 (DATA BASE ADDED FOR DATA)
