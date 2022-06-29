from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('posts/<int:pk>', views.post_detail, name='post_detail'),
    path('categories/<int:pk>', views.category_detail, name='category_detail'),
    path('add/', views.add, name='add'),
    path('register', views.register, name='register'),
    path('log_in', views.log_in, name='log_in'),
    path('log_out', views.log_out, name='log_out'),
    path('direct', views.direct, name='direct'),
    path('acc', views.acc, name='acc'),
    path('add_comment', views.add_comment, name='add_comment'),
    path('action', views.action, name='action')
]
