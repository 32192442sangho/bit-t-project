from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser


# Create your views here.

@api_view(['POST'])
@parser_classes([JSONParser])
def users(request):
    if request.method == 'POST':
        user_info = request.data
        name = user_info['Name']
        print(f'리액트에서 보낸 데이터 {user_info}')
        print(f'넘어온 이름 {name}')
        return JsonResponse({'name' : name})
    else: print('None')