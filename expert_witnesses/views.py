from django.shortcuts import render

from .models import AreaOfExpertise, Expert


def browser(request):
    filters = AreaOfExpertise.objects.all().order_by('field')
    filter = filters.filter(field=request.POST.get('filter')).values_list('field')
    experts = Expert.objects.all()
    if filter:
        experts = experts.filter(expertise__in=filter)

    return render(request, 'expertBrowser.html', {'experts': experts, 'filters': filters})


def viewer(request, id):
    expert = Expert.objects.get(id=id)
    return render(request, 'expertViewer.html', {'expert': expert})
