from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser


# Create your views here.

@api_view(['POST'])
@parser_classes([JSONParser])
def minimap_ward(request):
    if request.method == 'POST':
        return JsonResponse({'목록' : '하이'})
    else: print('None')
