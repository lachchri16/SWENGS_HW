from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CPUSerializer
from . import models


@api_view(['GET', 'POST'])
def cpu_default(request):
    if request.method == 'GET':
        cpus = models.CPU.objects.all()
        serializer = CPUSerializer(cpus, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CPUSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def cpu_pk(request, pk):
    try:
        cpu = models.CPU.objects.get(pk=pk)
    except models.CPU.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CPUSerializer(cpu)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CPUSerializer(cpu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cpu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
