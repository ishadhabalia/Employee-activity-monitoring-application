import logging
from rest_framework.views import APIView
from rest_framework import renderers
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from ets.apis.services.get_user_data import get_complete_user_data

logger = logging.getLogger(__name__)

class GetData(APIView):
    
    parser_classes = (JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    
    def get(self, request):
        user_id = request.auth_user_id
        logger.info('request is  {}'.format(user_id))
        user_activity_data = get_complete_user_data(user_id)
        return Response(user_activity_data)
                                                                                    