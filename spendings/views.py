from .models import Spending
from .serializers import SpendingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 

@api_view(['GET','POST'])
def spendings(request, format=None):
    if request.method == 'GET':
        spendings_list = Spending.objects.all()
        serializer = SpendingSerializer(spendings_list, many=True)
        return Response({"results":serializer.data})
    if request.method == 'POST':
        serializer = SpendingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['GET','PUT','DELETE'])
def spending_details(request, id, format=None):

    try:
        spending = Spending.objects.get(pk=id)
    except Spending.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SpendingSerializer(spending)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SpendingSerializer(spending, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        spending.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)