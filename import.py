import os, sys, string, csv, datetime, time, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thefts.settings")

from django.conf import settings

from reports.models import Location, CrimeType, Report

from django.template.defaultfilters import slugify, urlize

django.setup()

reader = csv.reader(open("THEFT.CSV", "rU"), dialect=csv.excel)

reader.next()

for row in reader:
    dateparseexample = time.strptime(row[0], "%m-%d-%Y")

    dateexample = datetime.datetime(dateparseexample.tm_year, dateparseexample.tm_mon, dateparseexample.tm_mday, dateparseexample.tm_hour, dateparseexample.tm_min)
    loc, loccreated = Location.objects.get_or_create(location = row[1], location_slug = slugify(row[1]))
    los = int(row[2])
    rec = int(row[3])
    ct, ctcreated = CrimeType.objects.get_or_create(crime_type = row[5], crime_type_slug = slugify(row[5]))
    rep, repcreated = Report.objects.get_or_create(report_date = dateexample, location = loc, loss = los, recovered = rec, crime_type = ct)
    print rep
