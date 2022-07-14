from rest_framework import serializers
from .models import Alert
from rest_framework.response import Response


class AlertSerializer(serializers.ModelSerializer):
    """
        _summary_

        AlertSerializer: Used to serilaizing Alert
        status :state of alert 

        fields: [price and status]

    """

    class Meta:
      model = Alert
      fields = ['price','status']
    
    def validate(self, data):
      user=self.context['request'].user
      if Alert.objects.filter(price=data['price'],user=user).exists():
        raise serializers.ValidationError(f"Alert already exists with price: {data['price']}")
      return data



class DeleteAlertSerializer(serializers.ModelSerializer):
    """
        _summary_

        DeleteAlertSerializer: Used to Deleting alert

    """
    class Meta:
      model = Alert
      fields = ['status']  