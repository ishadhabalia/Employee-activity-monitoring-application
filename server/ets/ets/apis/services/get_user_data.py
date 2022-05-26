from dashboard.models import UserBufferData, UserBufferLocation, UserBuffer
from rest_framework.exceptions import NotFound
from ets.apis.serializers.user_buffer_serializer import UserBufferSerializer, UserBufferLocationSerializer, UserBufferDataSerializer

def get_user_data(user_id):
    try:
        user_buffer = UserBuffer.objects.get(user_id=user_id)
        return UserBufferSerializer(instance=user_buffer).data
    except UserBuffer.DoesNotExist:
        raise NotFound(details="User not found",code=404)
    
def get_user_activity_data(user_id):
    try:
        user_buffer_activity = UserBufferData.objects.get(user_id=user_id)
        return UserBufferDataSerializer(instance=user_buffer_activity).data
    except UserBufferData.DoesNotExist:
        return None

def get_user_location(user_id):
    try:
        user_location = UserBufferLocation.objects.get(user_id=user_id)
        return UserBufferLocationSerializer(instance=user_location).data
    except UserBufferLocation.DoesNotExist:
        return None

def get_complete_user_data(user_id):
    user_details = get_user_data(user_id)
    user_activity_data = get_user_activity_data(user_id)
    user_location = get_user_location(user_id)
    return {"details": user_details,"activity": user_activity_data,"location": user_location}
    
        