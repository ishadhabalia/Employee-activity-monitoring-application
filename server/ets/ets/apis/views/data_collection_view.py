import logging
from rest_framework.views import APIView
from rest_framework import renderers
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from ets.apis.services.insert_user_data import insert_user_activity
from dashboard.services.get_user_data import get_user_buffer

logger = logging.getLogger(__name__)

class CollectData(APIView):
    
    parser_classes = (JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    
    def post(self, request):
        try:
            print(request.data)
            # user_id = request.auth_user_id
            user_id=2
            user_buffer = get_user_buffer(user_id)
            if user_buffer.break_status == 1:
                return Response({'status':'user on break'})
            logger.info("request is {}".format(request))
            is_data_added = insert_user_activity(user_id,request.data)
            if is_data_added:
                return Response({"status":"activity updated"})
            return Response({"status":"activity not updated"})
        except:
            raise Exception('user activity not saved')

# For stopping data collection when break is selected
class ToggleBreak(APIView):
    parser_classes = (JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request):
        strData = request.data
        print(strData)
        try:
            # if 0, stop tracking
            #if 1, resume tracking
            user_id = 2
            user = get_user_buffer(user_id)
            user.break_status = not user.break_status 
            user.save()
            return Response({"status":"toggle successful"})
        except:
            return Response({"status":"toggle unsuccessful"})

class ToggleProdCategory(APIView):
    parser_classes = (JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request):
        strData = request.data
        print(strData)
        try:
            # if 0, set to unproductive
            #if 1, set to productive
            return Response({"status":"toggle successful"})
        except:
            return Response({"status":"toggle unsuccessful"})
            