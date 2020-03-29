import pdb
from django.http import JsonResponse
from ..models.puzzle import Puzzle
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
class PuzzleView(APIView):
    def get(self, request):
        # puzzles = Puzzle.objects.all()
        puzzles = serializers.serialize('json', list(Puzzle.objects.all()))
        # for i, item in enumerate(puzzles):
        #     puzzles[i] = json.dumps(item)
        return Response(puzzles)