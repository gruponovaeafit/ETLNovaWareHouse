from src.comparator import Comparator
import pytest
from datetime import datetime

@pytest.mark.parametrize(
    [
        (Card(cardId='6434ec5be502e715cf661265', 
              listId='63f02f3229c0bc3d8173158f',
              membersId=['63f2ca4d791e17971239f926','63f2a578bb97677b68d2f8c7','5e4572c48caf2277dbfb0274','63fcd0afcce26c636b6bc425'],
              labelId='63f0355e416bd7f1dd8a88fc',
              endDate=datetime.strptime('2023-04-21 19:00:00','%Y-%m-%d %H:%M:%S')),
         Card(cardId='6434ec5be502e715cf661265', 
              listId='63f02f3229c0bc3d8173158f',
              membersId=['63f2ca4d791e17971239f926','63f2a578bb97677b68d2f8c7','5e4572c48caf2277dbfb0274','63fcd0afcce26c636b6bc425'],
              labelId='63f0355e416bd7f1dd8a88fc',
              endDate=datetime.strptime('2023-04-21 19:00:00','%Y-%m-%d %H:%M:%S')), 
         True),
        (Card(cardId='63f075d84189e9f728eae1ff', 
              listId='63f0355e416bd7f1dd8a88fc',
              membersId=['63f2ca4d791e17971239f926','63f2a578bb97677b68d2f8c7','5e4572c48caf2277dbfb0274','63fcd0afcce26c636b6bc425'],
              labelId='63f0355e416bd7f1dd8a88fc',
              endDate=datetime.strptime('2023-04-21 19:00:00','%Y-%m-%dT%H:%M:%S.%fZ')),
         Card(cardId='6434ec5be502e715cf661265', 
              listId='63f0355e416bd7f1dd8a88fc',
              membersId=['63f2ca4d791e17971239f926','63f2a578bb97677b68d2f8c7','5e4572c48caf2277dbfb0274','63fcd0afcce26c636b6bc425'],
              labelId='63f0355e416bd7f1dd8a88fc',
              endDate=datetime.strptime('2023-04-21 19:00:00','%Y-%m-%dT%H:%M:%S.%fZ')), 
         False)
    ]
)
def test_compareCards(card1, card2, expectedResult):
    assert Comparator.compareCards(card1, card2) == expectedResult
       