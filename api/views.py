from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student, Subject
from .serializers import StudentSerializer, SubjectSerializer


@api_view(['GET'])
def get_students(request):
    students = Student.objects.all()[:10]
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_subjects(request):
    subjects = Subject.objects.all().order_by('year')
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data)

