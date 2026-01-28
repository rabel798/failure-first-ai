from django.shortcuts import render
from rest_framework.views import APIView
from .models import Metric
from rest_framework.response import Response
from rest_framework import status
from .serializers import MetricSerialzer
# Create your views here.
class MetricView(APIView):
    
    def post(self,request):
        