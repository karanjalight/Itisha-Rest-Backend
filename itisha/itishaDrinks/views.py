from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from .models import *
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.shortcuts import render
from .serializers import *



#this view is to dirrect about all the existing urls
@api_view([ 'GET' ])
def apiOverview(request):

    api_urls = {
        'Mzinga': '/mzinga/',
        'Drinks': '/drinks/',
        'MzingaDetailView': 'mzinga/<str:slug>/',
        'DrinksDetailView': 'drinks/<str:pk>/',
    }
    return Response(api_urls)



#====================================== MZINGA ======================================#

# Mzinga list view 🍺🍺🍺🍻🍻
@api_view([ 'GET' ])
def mzingaList(request):
    mzinga = alcohol_drinks.objects.all()
    serializer = alcoholSerializer(mzinga, many=True)

    return Response(serializer.data)

# Mzinga detail view  🍺🍺🍺🍻🍻
@api_view([ 'GET' ])
def mzingaDetail(request, slug):
    mzinga = alcohol_drinks.objects.get(drink_slug=slug)
    serializer = alcoholSerializer(mzinga, many=False)

    return Response(serializer.data)


# Mzinga create    🍺🍺🍺🍻🍻
@api_view([ 'POST' ])
def mzingaCreate(request):
    if request.method == 'POST':
        serializer = alcoholSerializer(data= request.data)

        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
        else:
            return Response(serializer.errors)


        

# Mzinga update    🍺🍺🍺🍻🍻
@api_view([ 'POST' ])
def mzingaUpdate(request, slug):
   mzinga = alcohol_drinks.objects.get(drink_slug=slug)
   
   if request.method == 'POST':
    serializer = alcoholSerializer( instance=mzinga, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
     


   

# Mzinga delete  🍺🍺🍺🍻🍻
@api_view([  'DELETE' ])
def mzingaDelete(request, drink_slug):

   mzinga = alcohol_drinks.objects.get(drink_slug=drink_slug)
   serializer = alcoholSerializer( instance=mzinga, data=request.data)
   mzinga.delete()

   if serializer.is_valid():
        mzinga.delete()

   

   return Response(serializer.data)


#====================================== DRINKS ======================================#

# Mzinga list view 🍺🍺🍺🍻🍻
@api_view([ 'GET' ])
def drinkList(request):
    mzinga = itisha_drinks.objects.all()
    serializer = drinksSerializer(mzinga, many=True)

    return Response(serializer.data)

# Mzinga detail view  🍺🍺🍺🍻🍻
@api_view([ 'GET' ])
def drinkDetail(request, slug):
    mzinga = itisha_drinks.objects.get(drink_slug=slug)
    serializer = drinksSerializer(mzinga, many=False)

    return Response(serializer.data)


# Mzinga create    🍺🍺🍺🍻🍻
@api_view([ 'POST' ])
def drinkCreate(request):
   
   serializer = drinksSerializer

   if serializer.is_valid():
        serializer.save()

   return Response(serializer.data)


# Mzinga update    🍺🍺🍺🍻🍻
@api_view([ 'POST' ])
def drinkUpdate(request, slug):
   mzinga = itisha_drinks.objects.get(drink_slug=slug)
   serializer = drinksSerializer( instance=mzinga, data=request.data)


   if serializer.is_valid():
        serializer.save()

   return Response(serializer.data)

# Mzinga delete  🍺🍺🍺🍻🍻
@api_view([  'DELETE' ])
def drinkDelete(request, drink_slug):

   mzinga = itisha_drinks.objects.get(drink_slug=drink_slug)
   serializer = drinksSerializer( instance=mzinga, data=request.data)
   mzinga.delete()

   if serializer.is_valid():
        mzinga.delete()

   

   return Response(serializer.data)





class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



























class DrinkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = itisha_drinks.objects.all()
    serializer_class = drinksSerializer

 

class AlcoholViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = alcohol_drinks.objects.all()
    serializer_class = drinksSerializer



class alcoholApiView(APIView):
    # add permission to check if user is authenticated
    # 

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        todos = alcohol_drinks.objects.all()
        serializer = alcoholSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
"""  permission_classes = [permissions.IsAuthenticated]
    # 2. Create this function should be imporved to add the mzingas to cart
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = alcoholSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  """



""" class drinksApiView(APIView):
    # add permission to check if user is authenticated
    # 

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        todos = itisha_drinks.objects.all()
        serializer = drinksSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
 """
    
"""  permission_classes = [permissions.IsAuthenticated]
    # 2. Create this function should be imporved to add the mzingas to cart
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = alcoholSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  """







from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})


@api_view(['GET', 'POST'])
def drinksApiView(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})