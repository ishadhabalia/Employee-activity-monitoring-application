from rest_framework import serializers
from ets.apis.models import UserBuffer, UserBufferLocation, UserBufferData

class UserBufferSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBuffer
        fields = ('id', 'account_status','name', 'role', 'team','joined_on',)
    
class UserBufferDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBufferData
        fields = ('id','user_id','date','process_name',)

class UserBufferLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBufferLocation
        fields = ('id', 'user_id', 'ip', 'city','latitude', 'longitude')