from django.conf.urls.defaults import *

from profiles import views


urlpatterns = patterns('',
                       url(r'^create/$',
                           views.create_profile,
                           name='profiles_create_profile'),
                       url(r'^edit/$',
                           views.edit_profile,
                           name='profiles_edit_profile'),
                       url(r'(?P<username>\w+)/$',
                           views.profile_detail,
                           name='profiles_profile_detail'),
                       )
