from django.db.models import Count
from django.shortcuts import render

from .models import Region, Attorney


def index(request, id):
    attorney = Attorney.objects.get(id=id)
    return render(request, 'attorney.html', {'attorney': attorney})


def all(request):
    region = Region.objects.all().order_by('name')
    attorneys = Attorney.objects.all().annotate(Count('region'))
    return render(request, 'all.html', {'region': region, 'attorneys': attorneys})
