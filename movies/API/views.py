# views.py

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from django.contrib.auth.models import User
from .models import Movie, Collection, UserProfile
from .serializers import MovieSerializer, CollectionSerializer, UserProfileSerializer


# myapp/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def request_count(request):
    counter_key = 'request_counter'
    counter = cache.get(counter_key, 0)
    return Response({'requests': counter})

@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])  # Restrict access to admin users
def reset_request_count(request):
    counter_key = 'request_counter'
    cache.set(counter_key, 0, None)
    return Response({'message': 'Request count reset successfully'})


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register_user(request):
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.create_user(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        profile = UserProfile.objects.create(user=user)
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        return Response({'access_token': access_token}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieListView(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        # Implement movie listing logic here (calling third-party API)
        # ...

class CollectionListView(generics.ListAPIView):
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Implement collection listing logic here
        # ...

class CollectionCreateView(generics.CreateAPIView):
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Implement collection creation logic here
        # ...

class CollectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        pass



