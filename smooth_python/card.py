"""
一摞Python风格的纸牌
"""
import collections
from random import choice

# 自Python 2.6开始，namedtuple就加入到Python里，用以构建只有少数属性但是没有方法的对象，比如数据库条目。
# Card类表示一张纸牌
Card = collections.namedtuple("Card", ['rank', 'suit'])


# FrenchDesk类表示一副牌
class FrenchDesk:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# 创建一副牌
deck = FrenchDesk()
# 用len() 函数来查看一叠牌有多少张
print(len(deck))
# 抽取第一张牌和最后一张牌, 这都是由__getitem__方法提供的
print(deck[0], deck[-1])
# 抽取任意一张牌, Python已经内置了从一个序列中随机选出一个元素的函数random.choice
print(choice(deck))
