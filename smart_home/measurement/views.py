# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorsSerializer, MeasurementSerializer


class SensorsView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        data = SensorsSerializer(sensors, many=True)
        return Response(data.data)

    def post(self, request):
        title = request.data.get("title")
        description = request.data.get("description")
        Sensor(title=title, description=description).save()
        return Response(Sensor.data, status=status.HTTP_201_CREATED)

    # def path(self, request):


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer

    def patch(self, request, *args, **kwargs):
        pk = kwargs['pk']
        try:
            exampl = Sensor.objects.get(id=pk)
        except:
            return Response({'ошибка': "нет такого датчика"})
        ser = SensorsSerializer(exampl, data=request.data, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        sensor = Sensor.objects.get(id=pk)
        ser = SensorsSerializer(sensor)
        return Response(ser.data)


class MeasurementView(APIView):

    def post(self, request):
        ser = MeasurementSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)