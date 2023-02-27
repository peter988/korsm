from django.db import models

# Create your models here.
class men(models.Model):
    disc = models.TextField()
    price = models.TextField()
    image = models.TextField()
    image1 = models.TextField()
    cat = models.TextField()


class women(models.Model):
    disc = models.TextField()
    price = models.TextField()
    image = models.TextField()
    image1 = models.TextField()
    cat = models.TextField()

class kids(models.Model):
    disc = models.TextField()
    price = models.TextField()
    image = models.TextField()
    image1 = models.TextField()
    cat = models.TextField()

class handbags(models.Model):
    disc = models.TextField()
    price = models.TextField()
    image = models.TextField()
    image1 = models.TextField()
    cat = models.TextField()


class shoes1(models.Model):
    disc = models.TextField()
    price = models.TextField()
    image = models.TextField()
    image1 = models.TextField()
    cat = models.TextField()