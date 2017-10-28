
from django.db import models
# Leverage Django's built-in User models
from django.contrib.auth.models import User

# Create your models here.
class Ishar(models.Model):
    user =  models.ForeignKey(User, null=True, blank=True)
    description = models.CharField(max_length=128, null=False, blank=False)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        """this sets the default return for this object"""
        return self.description

class meditations(models.Model):
    Key = models.CharField(max_length=9)
    ItemType = models.CharField(max_length=15)
    Publication = models.IntegerField()
    Author = models.CharField(max_length=200)
    Title = models.CharField(max_length=300)
    PublicationTitle = models.CharField(max_length=500)
    ISSN = models.CharField(max_length=9)
    DOI = models.CharField(max_length=200)
    AbstractNote = models.TextField()
    Date = models.CharField(max_length=20)
    DateAdded = models.CharField(max_length=50)
    DateModified = models.CharField(max_length=50)
    Pages = models.CharField(max_length=50)
    Issue = models.IntegerField()
    JournalAbbreviation = models.CharField(max_length=200)
    ShortTitle = models.CharField(max_length=200)
    Language = models.CharField(max_length=3)
    LibraryCatalog = models.CharField(max_length=20)
    Extra = models.CharField(max_length=200)
    LinkAttachment = models.CharField(max_length=200)
    AutomaticTags = models.CharField(max_length=300)
    


    def __str__(self):
        """this sets the default return for this object"""
        return self.description
