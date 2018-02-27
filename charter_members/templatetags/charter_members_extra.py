from django import template


register = template.Library()


@register.filter
def filter_region(things, args):
    return things.filter(region=args)
