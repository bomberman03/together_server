from models import User, Project, Task, Feed
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField


class FeedSerializer(ModelSerializer):
    class Meta:
        model = Feed
        field = ('id', 'task', 'user', 'summary')


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        field = ('id', 'project', 'user', 'name', 'summary', 'end_date')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        field = ('id', 'student_id', 'department_name', 'grade', 'name', 'phone_number')


class ProjectSerializer(ModelSerializer):
    tasks = PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Project
        field = ('id', 'name', 'summary', 'start_date', 'end_date', 'users', 'tasks')


class ProjectNestedSerializer(ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        field = ('id', 'name', 'summary', 'start_date', 'end_date', 'users')
        depth = 1
