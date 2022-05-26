from dashboard.models import UserBuffer, UserBufferData, UserBufferLocation
from datetime import date

def get_user_buffer(user_id):
    try:
        return UserBuffer.objects.get(id=user_id)
    except UserBuffer.DoesNotExist:
        return None
        raise Exception('user not found: %s' % user_id)

def get_user_data(user):
    try:
        return UserBufferData.objects.filter(user_id=user)
    except UserBufferData.DoesNotExist:
        return list()
    except Exception as e:
        raise Exception('Something went wrong : {}'.format(e))

def get_user_location(user_id):
    try:
        return UserBufferLocation.objects.get(user_id=user_id).city
    except Exception as e:
        print(e)
        return None
