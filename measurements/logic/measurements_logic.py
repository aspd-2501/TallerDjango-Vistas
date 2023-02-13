from variables.models import Variable
from ..models import Measurement
from variables.logic.variables_logic import get_variable

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(measurement_pk):
    measurement = Measurement.objects.get(pk=measurement_pk)
    return measurement

def update_measurement(measurement_pk, new_measurement):
    measurement = get_measurement(measurement_pk)
    measurement.name = new_measurement["name"]
    measurement.save()
    return measurement

def create_measurement(measurement):
    variables_pk = Variable.objects.get(pk=measurement["variable"])
    measurement = Measurement(variable=variables_pk, value=measurement["value"], unit=measurement["unit"], place=measurement["place"])
    measurement.save()
    return measurement

def delete_measurement(measurement_pk):
    measurement = get_measurement(measurement_pk)
    measurement.delete()

def delete_measurements():
    measurements = Measurement.objects.all()
    for measurement in measurements:
        measurement.delete()
    