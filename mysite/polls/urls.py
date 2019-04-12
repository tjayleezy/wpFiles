from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/EECS/    
    path('<str:dept_code>/', views.dept_detail, name='dept_detail'),
    path('<str:dept_code>/EECS/',views.class_detail,
        name='EECS'),
    
]
