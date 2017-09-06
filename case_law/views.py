from django.shortcuts import render

from .models import Case, Heading


def browser(request):
    headings = {}
    path = request.GET.get('path')
    filter = request.GET.get('filter')
    cases = Case.objects.all()
    if filter:
        filter = filter.split('/')
        print(filter)
        ids = Heading.objects.filter(name__in=filter).values_list('id')
        for id in ids:
            cases = cases.filter(headings__in=id)
    elif path:
        path = path.split('/')
        ids = Heading.objects.filter(name__in=path).values_list('id')
        for id in ids:
            cases = cases.filter(headings__in=id)

    headings = set()
    for decision in cases:
        headings = headings.union(decision.headings.all().values_list('name', flat=True))
    if path: headings = headings.difference(path)

    return render(request, 'browser.html', {
        'allHeadings': Heading.objects.all().order_by('name'),
        'cases': cases.order_by('synopsis'),
        'caseCount': len(cases),
        'filter': filter,
        'headings': sorted(headings),
        'headingCount': len(headings),
        'url': request.GET.get('path'),
        'urls': path
    })


def case(request, id):
    case = Case.objects.get(id=id)
    return render(request, 'case.html', {'case': case, 'headings': case.headings.all()})
