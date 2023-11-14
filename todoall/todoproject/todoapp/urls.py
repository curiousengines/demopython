
from django.urls import path
from . import views

urlpatterns = [
   
    path ('', views.add,name='add'),
    path ('delete/<int:taskid>/', views.delete, name='delete'),
    path ('update/<int:id>/',views.update,name='update'),
    path ('cbvhome/', views.tasklist.as_view(), name='cvbhome' ),
    path ( 'cbvdetail/<int:pk>/', views.detail.as_view(), name='detail'),
    path ('cbvupdate/<int:pk>/', views.updatelist.as_view(), name='update'),
    path ( 'cbvdelete/<int:pk>/', views.deletelist.as_view(), name='detail'),
]
