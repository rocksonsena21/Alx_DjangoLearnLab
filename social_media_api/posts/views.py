from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


# Post ViewSet
class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter
    ]

    search_fields = ['title', 'content']


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



# Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)




from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])

def feed(request):

    users_followed = request.user.following.all()

    posts = Post.objects.filter(
        author__in=users_followed
    ).order_by('-created_at')

    serializer = PostSerializer(
        posts,
        many=True
    )

    return Response(serializer.data)