from django.template.loader import render_to_string

from OACPL import settings


def url_fix_render_to_string(template, context):
    temp = render_to_string(template, context)
    return temp.replace('src="/', 'src="%s/' % settings.BASE_URL).replace('href="/', 'href="%s/' % settings.BASE_URL)
