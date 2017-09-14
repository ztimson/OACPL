from django.shortcuts import render

from .models import Case, Heading


def browser(request):
    path = request.GET.get('path')
    cases = Case.objects.all()
    if path:
        path = path.split('/')
        ids = Heading.objects.filter(name__in=path).values_list('id')
        for id in ids:
            cases = cases.filter(headings__in=id)

    headings = set()
    for decision in cases:
        headings = headings | set(decision.headings.all().values_list('name', flat=True))
    if path: headings = headings.difference(path)

    return render(request, 'browser.html', {
        'allHeadings': Heading.objects.all().order_by('name'),
        'cases': cases.order_by('published'),
        'caseCount': len(cases),
        'headings': sorted(headings),
        'headingCount': len(headings),
        'url': request.GET.get('path'),
        'urls': path
    })
