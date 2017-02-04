from datetime import datetime, date, time

from analyzer.rating.model import Author
from analyzer.rating.model import Article

class TestModel:
    def test_author_name(self):
        a = Author("Kai", 3)
        assert a.name == "Kai"

    def test_article_name(self):
        a = Author("Kai", 3)
        d = date(2017, 2, 4)
        t = time(13, 22)
        article = Article(a, datetime.combine(d, t), 10)
        assert article.author == a
        assert article.rank_in_topic == 10
        assert article.published_time.year == 2017



