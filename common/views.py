from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.utils.user_groups import create_administrator_groups
from common.utils.user_groups import create_resource_groups


@api_view(['GET'])
def index(request):
    create_resource_groups()
    create_administrator_groups()
    response = {'message': 'Initial setup complete.'}

    return Response(response)
