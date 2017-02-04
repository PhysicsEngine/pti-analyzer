# -*- coding: utf-8 -*-

class Author(object):
    '''
    Author represents a author of article which keeps
    rating of the author.
    '''
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

class Article(object):
    '''
    Article represents a article by a author.
    '''
    def __init__(self, author, published_time, topics):
        self.author = author
        self.published_time = published_time
        # Topics is a list of tuple of topic category and probability.
        # e.g. [(1, 0.12), (2, 0.14), (3, 0.98),...]
        self.topics = topics