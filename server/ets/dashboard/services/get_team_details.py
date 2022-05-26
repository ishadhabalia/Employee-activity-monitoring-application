from dashboard.models import UserBuffer, UserBufferData, UserBufferLocation


def get_team_details():
    try:
        return UserBuffer.objects.exclude(role="manager")
    except Exception as e:
        print(e)
        return None
