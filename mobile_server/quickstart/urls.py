from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from views import UserList, UserDetail, ProjectList, ProjectNestedList, ProjectDetail, TaskList, TaskDetail, FeedList, FeedDetail

urlpatterns = [
    url(r'^nest/users/$', UserList.as_view()),
    url(r'^nest/users/(?P<phone_number>\+[0-9]+)/$', UserDetail.as_view()),
    url(r'^nest/projects/$', ProjectNestedList.as_view()),
    url(r'^nest/projects/(?P<users>[0-9]+)/$', ProjectDetail.as_view()),

    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<phone_number>\+[0-9]+)/$', UserDetail.as_view()),
    url(r'^projects/$', ProjectList.as_view()),
    url(r'^projects/(?P<pk>[0-9]+)/$', ProjectDetail.as_view()),
    url(r'^tasks/$', TaskList.as_view()),
    url(r'^tasks/(?P<pk>[0-9]+)/$', TaskDetail.as_view()),
    url(r'^feeds/$', FeedList.as_view()),
    url(r'^feeds/(?P<pk>[0-9]+)/$', FeedDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)