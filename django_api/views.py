from rest_framework import status, permissions, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .models import Movie  # Import the Movie model

# Serializer for movie data
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'  # Include all fields from the Movie model

# API endpoint for managing movies
class MovieAPI(APIView):
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(request_body=MovieSerializer)
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the movie instance
            return Response(
                data={"status": "OK", "message": "Movie created successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        movies = Movie.objects.all()  # Retrieve all movies
        serializer = MovieSerializer(movies, many=True)  # Serialize the movie data
        return Response(serializer.data, status=status.HTTP_200_OK)
