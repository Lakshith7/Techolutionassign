from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from rest_framework.views import APIView
from rest_framework import status
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def TodoView(request):
    if request.method == 'GET':
        data = Todo.objects.all().values()
        a=[]
        for i in data:
            b=[]
            for j in i:
                if j=='id':
                    pass
                elif j=="catname":
                    if i[j]=='[]':
                        break
                    else:
                        b.append(json.loads(i[j]))
                else:
                    b.append(i[j])
            if b:
                a.append(b)
        final=[]
        for h in a:
            name=h[1]
            ah=sorted(h[0], key=lambda x: x[-1], reverse=True)
            colour=ah[0][-1]
            co1=0
            c=[]
            c.append([colour])
            for i1 in range(len(ah)):
                if ah[i1][-1]==colour:
                   c[co1].append(ah[i1][0])
                else:
                    colour=ah[i1][-1]
                    co1+=1
                    c.append([colour,ah[i1][0]])
            for k in c:
                k.insert(0, name)
            final.extend(c)
        serializer = TodoSerializer(data, context={'request': request}, many=True)
        print(final)
        return Response(final)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)