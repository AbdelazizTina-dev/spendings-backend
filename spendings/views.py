from .models import Spending
from .serializers import SpendingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 

@api_view(['GET','POST'])
def spendings(request):
    if request.method == 'GET':
        spendings_list = Spending.objects.all()
        serializer = SpendingSerializer(spendings_list, many=True)
        return Response({"results":serializer.data})
    if request.method == 'POST':
        serializer = SpendingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)