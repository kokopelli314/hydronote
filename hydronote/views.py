from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from django.http import Http404

from rest_framework import generics, permissions, status
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Note
from .forms import NoteForm
from .serializers import NoteSerializer


# Home route
def index(request):
    return render(request, 'hydronote/base_angular.html')


class NoteList(APIView):
    """
    List all notes, or create a new note.
    """
    def get(self, request, format=None):
        notes = Note.objects.all().filter(author__username=self.request.user)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetail(APIView):
    """
    Retrieve, update, or delete a note.
    """
    permission_classes = (permissions.AllowAny,)
    def get_object(self, pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            raise Http404
            
    def get(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        print("--------------NoteDetail.put called")
        note = self.get_object(pk)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
        
