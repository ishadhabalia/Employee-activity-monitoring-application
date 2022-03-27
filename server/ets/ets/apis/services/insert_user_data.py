from ets.apis.models import UserBufferData, UserBufferLocation
import ets.apis.constants as Constants

def get_user_buffer_location_data(user_id):
    try:
        user_buffer_location_data = UserBufferLocation.objects.get(user_id=user_id)
        return user_buffer_location_data
    except UserBufferLocation.DoesNotExist:
        return None

def create_user_buffer_location(user_id, data):
    try:
        user_buffer_location_data = UserBufferLocation(user_id=user_id, ip=data.ip, city=data.city, latitude=data.latitude, longitude=data.longitude)
        user_buffer_location_data.save()
    except:
        raise Exception("Location Data could not be intialized")

def update_user_location(instance, data):
    try:
        instance.ip = data.ip
        instance.latitude = data.latitude
        instance.longitude = data.longitude
        instance.city = data.city
        instance.save()
    except:
        raise Exception("Location Data could not be updated")
        

def update_user_location(user_id,data):
    try:
        user_buffer_location_data = get_user_buffer_location_data(user_id)
        if user_buffer_location_data is None:
            create_user_buffer_location(user_id,data)
        else:
            update_user_location(user_buffer_location_data, data)
            return True
    except:
        return False
        
    

def insert_user_activity(user_id,data):
    if data.keys() != Constants.ACTIVITY_DATA.keys():
        raise Exception("Wrong data format")
    try:
        user_activity_data = UserBufferData(user_id=user_id,process_name=data.process_name,date=data.date)
        user_activity_data.save()
        # TODO: import the methods for classificaiton and append the values in the model @isha & @mahi
        if not update_user_location(user_id,data):
            raise Exception("Wrong location data")
        return True
    except:
        return False