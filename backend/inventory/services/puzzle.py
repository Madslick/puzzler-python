from ..models.puzzle_theme import PuzzleTheme
from ..models.puzzle import Puzzle

def puzzle():
    if PuzzleService._instance is None:
        PuzzleService._instance = PuzzleService()
    return PuzzleService._instance

class PuzzleService():
    _instance = None
    
    def filter_puzzles(self):
        puzzles=Puzzle.object.all()
        return []