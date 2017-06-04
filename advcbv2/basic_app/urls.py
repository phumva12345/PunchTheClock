from django.conf.urls import url
from basic_app import views
from django.contrib.auth import views as vviews

app_name = 'basic_app'

urlpatterns = [
    url(r'^$',views.EmployeeListView.as_view(),name='list'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^(?P<pk>\d+)/$',views.EmployeeDetailView.as_view(),name='detail'),
    url(r'^create/$',views.EmployeeCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.EmployeeUpdateView.as_view(),name='update'),
    url(r'^departupdate/(?P<pk>\d+)/$',views.DepartmentUpdateView.as_view(),name='depupdate'),
    url(r'^delete/(?P<pk>\d+)/$',views.EmployeeDeleteView.as_view(),name='delete'),
    url(r'^deletedep/(?P<pk>\d+)/$',views.DepartmentDeleteView.as_view(),name='deletedep'),
    url(r'^accounts/login/$', vviews.login, name='login'),
    url(r'^accounts/logout/$', vviews.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^search/$',views.EmployeeSearchListView.as_view(),name='search_detail'),
    url(r'^creates/$',views.AttendanceCreateView.as_view(),name='createatt'),
    url(r'^createdeps/$',views.DepartmentCreateView.as_view(),name='createdep'),
    url(r'^deplist/$',views.DepartmentListView.as_view(),name='dlist'),
    url(r'^deplistdetail/(?P<pk>\d+)/$',views.DepartmentDetailView.as_view(),name='ddetail'),
    url(r'^helpsupport/$',views.HelpSupport.as_view(),name='help'),




]
