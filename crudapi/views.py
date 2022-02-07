from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Person
from .serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def Person_details(request):
    if request.method == 'GET':

        # json_data = request.body
        # stream = io.BytesIO(json_data)
        # pythondata = JSONParser().parse(stream)
        # id = pythondata.get('id',None)
        # if id is not None:
            # per = Person.objects.get(id=id)
            # Serializer = PersonSerializer(per)
            # json_data = JSONRenderer().render(Serializer.data)
            # return HttpResponse(json_data, content_type='application/json')
        per = Person.objects.all()
        Serializer = PersonSerializer(per, many=True)
       # json_data = JSONRenderer().render(Serializer.data)
        return JsonResponse(Serializer.data,safe=False)

    elif request.method=='POST':
        per = JSONParser().parse(request)
        Serializer = PersonSerializer(data = per)

        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse("added successfully",safe=False)
        return JsonResponse(Serializer.errors)
    
    elif request.method=='PUT':
        per = JSONParser().parse(request)
        
        id = per.get('id')
        print('hello')
        print(id)
        pers = Person.objects.get(id=1)
        serializer = PersonSerializer(pers,data=per,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("updated successfully",safe=False)
        return JsonResponse(Serializer.errors)
    elif request.method=='DELETE':
        per = JSONParser().parse(request)
        id = per.get('id')
        pers = Person.objects.get(id=1)
        pers.delete()
        return JsonResponse("deleted successfully",safe=False)
    return JsonResponse(Serializer.errors)
        



    # if request.method == 'POST':
    #    json_data = request.body
    # #    stream = io.BytesIO(json_data)
    # #    pythondata = JSONParser().parse(stream)
    #    Serializer = PersonSerializer(json_data)
    #    if Serializer.is_valid():
    #        Serializer.save()
    #        res = {'msg': 'Data Created'}
    #        json_data = JSONRenderer().render(res)
    #        return HttpResponse(json_data, content_types='application/json')
    # json_data= JSONRenderer().render(Serializer.errors)
    # return HttpResponse(json_data, content_types='application/jso')
        