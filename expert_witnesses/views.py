from django.shortcuts import render

from .models import AreaOfExpertise, Expert


def browser(request):
    filters = AreaOfExpertise.objects.all().order_by('field')

    experts = Expert.objects.all()

    institutes = set()
    for expert in experts:
        institutes.add(expert.institute) if expert.institute is not None else None

    if request.GET.get('name'):
        experts = experts.filter(name__contains=request.GET.get('name'))

    if request.GET.get('institute'):
        experts = experts.filter(institute=request.GET.get('institute'))

    if request.GET.get('experties'):
        experts = experts.filter(expertise=AreaOfExpertise.objects.filter(field=request.GET.get('experties'))).distinct()

    return render(request, 'expertBrowser.html', {'experts': experts, 'institutes': institutes, 'filters': filters})


def viewer(request, id):
    expert = Expert.objects.get(id=id)
    return render(request, 'expertViewer.html', {'expert': expert})
