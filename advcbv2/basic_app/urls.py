from django.conf.urls import url
from basic_app import views
from django.contrib.auth import views as vviews

app_name = 'basic_app'

urlpatterns = [
    url(r'^$',views.EmployeeListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.EmployeeDetailView.as_view(),name='detail'),
    url(r'^create/$',views.EmployeeCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.EmployeeUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.EmployeeDeleteView.as_view(),name='delete'),
    url(r'^accounts/login/$', vviews.login, name='login'),
    url(r'^accounts/logout/$', vviews.logout, name='logout', kwargs={'next_page': '/'}),

]
