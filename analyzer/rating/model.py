# -*- coding: utf-8 -*-

class Author:
    '''
    Author represents a author of article which keeps
    rating of the author.
    '''
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

class Article:
    '''
    Article represents a article by a author.
    '''
    def __init__(self, author, rank_in_topic):
        self.author = author
        self.rank_in_topic = rank_in_topic