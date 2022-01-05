from rest_framework import serializers
from api.models import Person, Course, Grade

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'courses')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'year')

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('person', 'course', 'grade')