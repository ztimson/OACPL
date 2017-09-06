from django.shortcuts import render

from .models import Decision, Subtitle


def browser(request):
    headers = {}
    path = request.GET.get('path')
    filter = request.GET.get('filter')
    decisions = Decision.objects.all()
    if filter:
        filter = filter.split('/')
        print(filter)
        ids = Subtitle.objects.filter(name__in=filter).values_list('id')
        for id in ids:
            decisions = decisions.filter(headers__in=id)
    elif path:
        path = path.split('/')
        ids = Subtitle.objects.filter(name__in=path).values_list('id')
        for id in ids:
            decisions = decisions.filter(headers__in=id)

    headers = set()
    for decision in decisions:
        headers = headers.union(decision.headers.all().values_list('name', flat=True))
    if path: headers = headers.difference(path)

    return render(request, 'browser.html', {
        'allHeaders': Subtitle.objects.all().order_by('name'),
        'decisions': decisions.order_by('synopsis'),
        'decisionsCount': len(decisions),
        'filter': filter,
        'headers': sorted(headers),
        'headersCount': len(headers),
        'url': request.GET.get('path'),
        'urls': path
    })


def case(request, id):
    decision = Decision.objects.get(id=id)
    return render(request, 'decision.html', {'decision': decision})
