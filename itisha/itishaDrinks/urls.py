from django.urls import path
from . import views

urlpatterns = [
    #This is the Mu' fucking home! 🏠🏠
    path('', views.apiOverview, name='api-overview'),

    #list views
    path('mzinga/', views.mzingaList, name='mzinga-list'),
    path('drinks/', views.drinkList, name='mzinga-list'),

    #detail views
    path('mzinga/<str:slug>/', views.mzingaDetail, name='mzinga-details'),
    path('drinks/<str:slug>/', views.drinkDetail, name='drinks-details'),

    #create views
    path('mzinga-create/', views.mzingaCreate, name='mzinga-create'),
    path('drink-create/', views.drinkCreate, name='drink-create'),

    #update
    path('drink-update/<str:slug>/', views.drinkUpdate, name='mzinga-update'),

    #delete
    path('mzinga-delete/<str:drink_slug>/', views.mzingaDelete, name='mzinga-delete'),
]
