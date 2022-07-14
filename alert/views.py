from django.shortcuts import render
from rest_framework.views import APIView
from .models import Alert
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import AlertSerializer,DeleteAlertSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework import generics
from alert.filters import CustomSearchFilter

class ListAlertAPIView(generics.ListAPIView):
    """
        _summary_

        ListAlertAPIView used to filter response based on status and price

        status :state of alert 

        price : price for triggering alert

    """
    permission_classes = [IsAuthenticated]
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'price']

    def get_queryset(self, *args, **kwargs):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset

class CreateAlertApiView(generics.GenericAPIView):
    """
        _summary_

        CreateAlertApiView used to createing alert

        price : price for creating alert

    """
    permission_classes = [IsAuthenticated]
    serializer_class = AlertSerializer
    def post(self, request, format=None):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class AlertDeleteApiView(generics.GenericAPIView):
    """
        _summary_

        AlertDeleteApiView used to delete alert

    """
    permission_classes = [IsAuthenticated]
    serializer_class = AlertSerializer
    
    def delete(self, request,pk, format=None):

        try:
            user= request.user
            alert=  Alert.objects.get(user=user,pk=pk)
            data = {'status': 'deleted'}
            serializer = DeleteAlertSerializer(alert, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)