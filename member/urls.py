from django.urls import path
from . import views
from django.http import HttpResponseRedirect

def redirect_to_admin(request):
    return HttpResponseRedirect('/admin/')

urlpatterns = [
    path('', redirect_to_admin),
    path('member/', views.member, name = 'member'),
    path('member/details/<int:id>', views.details, name= 'details'),
    path('chat', views.lobby, name="lobby")
]