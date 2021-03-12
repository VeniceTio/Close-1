
from Model.Articles import *

class ArticlesController:
    """Controle les listes d'articles"""

    def __init__(self):
        self.articles = []
        self.id = 0

    def addArticle(self, p_name, p_price, p_avaProd, p_seller, p_desc):
        newArticle = Articles(self.id, p_name, p_price, p_avaProd, p_seller, p_desc)
        self.id += 1
        self.articles.append(newArticle)

    def delArticle(self,id):

    def selectArticlesBySeller(self,p_seller):
        result = []
        for article in self.articles:
            if article.getSeller() == p_seller:
                result.append(article)
        return result

    def triByPrice(self):
        result = self.articles

