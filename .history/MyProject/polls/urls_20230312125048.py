from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('detail/<int:question_id>',views.detailView,name="detail"),
    path('',views.index,name='index'),
    path('list/',views.viewlist,name='view_list'),
    path('login/',views.loginView,name='login')
]