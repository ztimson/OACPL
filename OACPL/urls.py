import os

from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.shortcuts import Http404
from django.views.static import serve

import main.views
import case_law.views
import charter_members.views
import expert_witnesses.views
import newsletters.views


@login_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    if not request.user.has_perm('view_pdf'):
        return Http404()
    return serve(request, path, document_root, show_indexes)


urlpatterns = [
    url(r'^$', main.views.index, name='home'),
    url(r'^admin/logout', main.views.logout, name='logout'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^attorney/(?P<id>\d+)', charter_members.views.index, name='attorney'),
    url(r'^caselaw/', case_law.views.browser, name='caselaw'),
    url(r'^experts/', expert_witnesses.views.browser, name='experts'),
    url(r'^experts/(<?P<id>\d+)', expert_witnesses.views.viewer, name='expert'),
    url(r'^media/secure/(?P<path>.*)$', protected_serve, {'document_root': os.path.join(settings.MEDIA_ROOT, 'secure')}, name='secure media'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    url(r'^newsletter/subscribe', newsletters.views.subscribe, name='subscribe'),
    url(r'^newsletter/', newsletters.views.newsletters, name='newsletters'),
]
