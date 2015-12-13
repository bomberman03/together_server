from models import User, Project, Task, Feed
from serializers import UserSerializer, ProjectNestedSerializer, ProjectSerializer, TaskSerializer, FeedSerializer
from rest_framework import generics
from rest_framework import filters


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'phone_number'


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('users', )


class ProjectNestedList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectNestedSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('users', )


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('user', 'project')


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class FeedList(generics.ListCreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('task', )


class FeedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
