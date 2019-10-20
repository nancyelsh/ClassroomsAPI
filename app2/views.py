from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from classes.models import Classroom
from .serializers import ClassListSerializer, ClassDetailSerializer, ClassCreateSerializer, ClassUpdateSerializer

# Create your views here.

class ClassListView(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassListSerializer

class ClassDetailView(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassCreateView(CreateAPIView):
    serializer_class = ClassCreateSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class ClassUpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class ClassDeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'