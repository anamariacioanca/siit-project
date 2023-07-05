from rest_framework.serializers import HyperlinkedModelSerializer
from . models import Course

class CourseSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ["name", "time", "price"]