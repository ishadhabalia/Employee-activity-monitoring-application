import logging
from rest_framework.views import APIView
from rest_framework import renderers
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from ets.apis.services.insert_user_data import insert_user_activity

logger = logging.getLogger(__name__)

class CollectData(APIView):
    
    parser_classes = (JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    
    def post(self, request):
        try:
            print(request.data)
            # user_id = request.auth_user_id
            user_id=1
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
            return Response({"status":"toggle successful"})
        except:
            return Response({"status":"toggle unsuccessful"})
            