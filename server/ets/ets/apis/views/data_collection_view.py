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
            user_id = request.auth_user_id
            logger.info("request is {}".format(request))
            is_data_added = insert_user_activity(user_id)
            if is_data_added:
                return Response({"status":"activity updated"})
        except:
            raise Exception('user activity not saved')
            