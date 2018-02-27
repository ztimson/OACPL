from django.db.models import Count
from django.shortcuts import render

from .models import Region, Attorney
from .forms import AttorneyForm


def index(request, id):
    attorney = Attorney.objects.get(id=id)
    edit_form = AttorneyForm(request.POST or None, request.FILES or None, instance=attorney)
    if request.method == 'POST' and edit_form.is_valid():
        edit_form.save()
    return render(request, 'attorney.html', {'attorney': attorney, 'editForm': edit_form})


def all(request):
    region = Region.objects.all().order_by('name')
    attorneys = Attorney.objects.all().annotate(Count('region'))
    other = Attorney.objects.filter(region=None).count() > 0
    return render(request, 'all.html', {'region': region, 'attorneys': attorneys, 'other': other})
