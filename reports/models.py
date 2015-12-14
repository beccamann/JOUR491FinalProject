from django.db import models

class Location(models.Model):
    location = models.CharField(max_length=255)
    location_slug = models.SlugField()
    def __unicode__(self):
        return self.location
    def get_absolute_url(self):
        return "/locations/%s/" % self.location_slug

class CrimeType(models.Model):
    crime_type = models.CharField(max_length=255)
    crime_type_slug = models.SlugField()
    def __unicode__(self):     
        return self.crime_type
    def get_absolute_url(self):
        return "types/%s/" % self.crime_type_slug

class Report(models.Model):
    report_date = models.DateField()
    location = models.ForeignKey(Location)
    loss = models.IntegerField()
    recovered = models.IntegerField()
    crime_type = models.ForeignKey(CrimeType)
    def __unicode__(self):
        return "%i" % self.id
