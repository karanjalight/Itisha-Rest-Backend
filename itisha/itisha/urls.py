from django.urls import include, path
from rest_framework import routers
from itishaDrinks import views
from todo.views import *
from itishaDrinks.views import *

from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'drinks', views.DrinkViewSet)
router.register(r'alcohol', views.AlcoholViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path('api/', TodoListApiView.as_view(), name= "list"),          #the last time for real  😂😂
    path('alcohol', alcoholApiView.as_view(), name= "mzinga"),      #this view supports alcoholic drinks since they have a wider variety
    path('drinks', alcoholApiView.as_view(), name= "drinks"),       #this view supports drinks like sodas, yorghurt, energy drinks, coktails and other soft drinks with the similar



]