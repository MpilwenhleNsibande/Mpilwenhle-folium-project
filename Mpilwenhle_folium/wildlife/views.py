from django.shortcuts import render
from .models import Organisation, Property
from django.contrib.gis.geos import GEOSGeometry

def organisation_list(request):
    organisations = Organisation.objects.all()
    return render(request, 'wildlife/organisation_list.html', {'organisations': organisations})

def organisation_detail(request, pk):
    organisation = Organisation.objects.get(pk=pk)
    return render(request, 'wildlife/organisation_detail.html', {'organisation': organisation})

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'wildlife/property_list.html', {'properties': properties})

def property_detail(request, pk):
    property = Property.objects.get(pk=pk)
    return render(request, 'wildlife/property_detail.html', {'property': property})

def map_view(request):
    properties = Property.objects.all()
    # Pass properties to the template
    context = {'properties': properties}
    return render(request, 'map.html', context)
