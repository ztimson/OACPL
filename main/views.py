from django.shortcuts import render

from charter_members.models import Attorney


def index(request):
    attorneys = Attorney.objects.filter(front_page=True)
    return render(request, 'index.html', {'attorneys': attorneys})
