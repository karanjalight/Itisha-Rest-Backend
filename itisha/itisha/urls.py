from django.urls import include, path
from rest_framework import routers
from itishaDrinks import views
from todo.views import *
from itishaDrinks.views import *

from django.contrib import admin
from itishaDrinks import urls


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'drinks', views.DrinkViewSet)
router.register(r'alcohol', views.AlcoholViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
            

    path('', include('itishaDrinks.urls')), #the last time for real  😂😂






    #👉 This here is the list view for our products
         #this view supports drinks like sodas, yorghurt, energy drinks, coktails and other soft drinks with the similar



    #👉 This here is the list view for our products
    #path('mzinga/<str:slug>', alcoholDetailApiView.as_view(), name= "drinks"),
    #path('drinks/<str:slug>', drinkDetailApiView.as_view(), name= "drinks"),
    



]