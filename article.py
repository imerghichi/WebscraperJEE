"la classe contient le titre et le contenu des articles"

class Article(object):
    def __init__(self, id, title, link, description, rating):
        self.id = id
        self.title = title
        self.link = link
        self.description = description
        self.rating = rating

