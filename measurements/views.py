from .logic import measurements_logic as ml
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            variable_dto = ml.get_measurements(id)
            variable = serializers.serialize('json', [variable_dto,])
            return HttpResponse(variable, 'application/json')
        else:
            measurements_dto = ml.get_measurements()
            measurements = serializers.serialize('json', measurements_dto)
            return HttpResponse(measurements, 'application/json')

    if request.method == 'POST':
        variable_dto = ml.create_variable(json.loads(request.body))
        variable = serializers.serialize('json', [variable_dto,])
        return HttpResponse(variable, 'application/json')
    
    if request.method == 'DELETE':
        ml.delete_measurements()
        return HttpResponse("Measurements deleted", 'application/json')
    
@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'GET':
        variable_dto = ml.get_measurement(pk)
        variable = serializers.serialize('json', [variable_dto,])
        return HttpResponse(variable, 'application/json')

    if request.method == 'PUT':
        variable_dto = ml.update_variable(pk, json.loads(request.body))
        variable = serializers.serialize('json', [variable_dto,])
        return HttpResponse(variable, 'application/json')
    
    if request.method == 'DELETE':
        ml.delete_measurement(pk)
        return HttpResponse("Measurement deleted", 'application/json')
    
