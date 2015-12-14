from django.shortcuts import render
from django.db.models import Count

from reports.models import CrimeType, Report, Location

def index(request):
    crime_types = CrimeType.objects.annotate(Count('report')).order_by('-report__count')
    locations = Location.objects.annotate(Count('report')).order_by('-report__count')[:25]
    context = {'crime_types': crime_types, 'locations': locations}
    return render(request, 'index.html', context)

def typedetail(request, type_slug):
    crime_type = CrimeType.objects.get(crime_type_slug=type_slug)
    reports = Report.objects.filter(crime_type=crime_type, report_date__year=2014)
    context = {'crime_type': crime_type, 'reports': reports}
    return render(request, 'typedetail.html', context)

def locationtypedetail(request, type_slug, location_slug):
    crime_type = CrimeType.objects.get(crime_type_slug=type_slug)
    location = Location.objects.get(location_slug=location_slug)
    reports = Report.objects.filter(crime_type=crime_type, location=location)
    context = {'crime_type': crime_type, 'reports': reports, 'location': location}
    return render(request, 'locationtypedetail.html', context)

def locationdetail(request, location_slug):
    location = Location.objects.get(location_slug=location_slug)
    reports = Report.objects.filter(location=location)
    context = {'location': location, 'reports': reports}
    return render(request, 'locationdetail.html', context)



