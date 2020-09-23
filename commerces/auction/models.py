from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


class User(AbstractUser):
    pass


class listing(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    ImageUrl = models.CharField(max_length=100000)
    Image = models.ImageField(
        default="/static/auction/img/icon-3.png")
    Category = models.CharField(max_length=10000)
    Bid = models.IntegerField(default=0)
    Time = models.TimeField(default=datetime.datetime.now())
    List_Creator = models.CharField(max_length=500, default="Anonymous")

    def __str__(self):
        return f" Title: {self.Title}, Description: {self.Description}, ImageUrl: {self.ImageUrl}, Category: {self.Category}, Bid: ${self.Bid} {self.Time}"


class bids(models.Model):
    Start_Bid = models.IntegerField()
    Bidding = models.ManyToManyField(listing, blank=True, related_name="Bids")
    User_Bid = models.ManyToManyField(
        User, blank=True, related_name="User_Bidings")
    Bid_No = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.Start_Bid}"


class comment(models.Model):
    Comment = models.CharField(max_length=64)
    Comment_By = models.CharField(max_length=100, default="Anonymous")
    User_Comment = models.ManyToManyField(
        User, blank=True, related_name="Comments")
    List_Comment = models.ManyToManyField(
        listing, blank=True, related_name="Comment_For_Listing")

    # def __str__(self):
    #   return f"Comment: {self.Comment},  Made by: {self.Comment_By},  for {self.List_Comment}"


class watch(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    ImageUrl = models.CharField(max_length=100000)
    Image = models.ImageField(
        default="/static/auction/img/icon-3.png")
    Category = models.CharField(max_length=10000)
    Bid = models.IntegerField(default=0)
    Time = models.TimeField(default=datetime.datetime.now())
    List_Creator = models.CharField(max_length=500, default="Admin")

    def __str__(self):
        return f" {self.Title} /n {self.Description} /n {self.ImageUrl} /n {self.Category} {self.Bid} {self.Time}"


class notification(models.Model):
    Notifications = models.CharField(max_length=1000)
    User_To_Be_Notified = models.ManyToManyField(
        "User", blank=True, related_name="User_To_Be_Notifieds")
