from analyzer.rating.model import Author
from analyzer.rating.model import Article

class TestModel:
    def test_author_name(self):
        a = Author("Kai", 3)
        assert a.name == "Kai"

    def test_article_name(self):
        a = Author("Kai", 3)
        article = Article(a, 10)
        assert article.author == a
        assert article.rank_in_topic == 10

