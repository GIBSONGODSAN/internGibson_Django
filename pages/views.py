from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .models import User, UserProfile, Sport

from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.translation import gettext as _
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer

@authentication_classes('rest_framework_simplejwt.authentication.JSONWebTokenAuthentication')
@permission_classes([IsAuthenticated])
class UserView(APIView):
    def get(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def login(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        department = request.POST.get('department')
        sports = request.POST.get('sports')

        if action == 'SignIn':
            user = User.objects.filter(username=username, password=password).first()
            user_id = user.user_id
            sport_id = user.sports.sport_id
            if user is not None:
                user_profile = UserProfile.objects.filter(user_id=user_id).first()
                sport_name = Sport.objects.get(pk=sport_id).name if sport_id else None
                print(user_profile, sport_name)
                return render(request, 'home.html', {'user_profile': user_profile, 'sport_name': sport_name})
            else:
                return render(request, 'login.html', {'error': 'Invalid credentials'})

        elif action == 'SignUp':
            print(username, email)
            existing_user = User.objects.filter(username=username).exists()
            existing_email = User.objects.filter(email=email).exists()
            print(existing_user, existing_email)
            
            if not existing_user and not existing_email:
                print('creating new user')
                new_user = User.objects.create(username=username, email=email, password=password)
                new_user.save()
                new_user_profile = UserProfile.objects.create(user=new_user, department=department)
                new_user_profile.save()
                new_user.sports.add(sport_id)
                new_user.save()
                return redirect('home')
            else:
                return render(request, 'login.html', {'error': 'User with this username or email already exists'})

    return render(request, 'login.html') 

def home(request):
    return render(request, 'home.html')
