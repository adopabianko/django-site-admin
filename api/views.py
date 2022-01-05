from rest_framework import viewsets
from api.serializers import PersonSerializer, CourseSerializer, GradeSerializer
from api.models import Person, Course, Grade

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('first_name')
    serializer_class = PersonSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('name')
    serializer_class = CourseSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all().order_by('person')
    serializer_class = GradeSerializer