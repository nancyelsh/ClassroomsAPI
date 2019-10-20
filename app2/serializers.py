from rest_framework import serializers
from classes.models import Classroom


class ClassListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['subject', 'year', 'teacher']

class ClassDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = '__all__'

class ClassCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = '__all__'

class ClassUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = '__all__'