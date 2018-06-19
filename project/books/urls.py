from django.conf.urls import url
from books.views import BookList,BookDelete
from . import views
from django.conf import settings
from django.conf.urls.static import static
from books.views import BookUpdate

urlpatterns=[
    url(r'^$',views.home, name ='home'),
    url(r'^search/$',views.search_form, name = 'search'),
    url(r'^results/$', views.search_result, name= 'search_results'),
    url(r'^book/$', BookList.as_view(), name= 'book'),
    url (r'^update/$',views.get_name,name = 'get_name'),
    url(r'^upload/$',views.upload_file, name = 'upload'),
    # url books/book/3 starts from primary key 3
    url(r'^book/(?P<pk>[0-9]+)/$', BookUpdate.as_view(),
        name='book_update'),
        #url books/book/3/delete
    url(r'^book/(?P<pk>[0-9]+)/delete/$', BookDelete.as_view(),
        name='book_delete'),


]
