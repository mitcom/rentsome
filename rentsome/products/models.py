from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product)

    def __str__(self):
        return self.name


class RentalManager(models.Manager):
    def active(self):
        return self.get_queryset().filter(end=None)

    def received(self):
        return self.get_queryset().exclude(end=None)


class Rental(models.Model):
    begin = models.DateTimeField()
    end = models.DateTimeField()
    article = models.ForeignKey(Article, related_name='rentals')

    objects = RentalManager

    def __str__(self):
        return '{} ({b}-{e})'.format(
            self.article.name,
            b=self.begin,
            e=self.end,
        )
