from django.db.models import Count
from django.shortcuts import render

from .models import Chapter, Attorney


def index(request, id):
    attorney = Attorney.objects.get(id=id)
    return render(request, 'attorney.html', {'attorney': attorney})


def all(request):
    chapters = Chapter.objects.all().order_by('name')
    attorneys = Attorney.objects.all().annotate(Count('chapter'))
    return render(request, 'all.html', {'chapters': chapters, 'attorneys': attorneys})
