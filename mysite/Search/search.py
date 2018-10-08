from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Search



connections.create_connection()

class ArticleIndex(DocType):
     name = Text()
     shortDescription = Text()
     specialityNumber = Text()
     mainText = Text()

     class Meta:
         index = 'article-index'

def bulk_indexing():
     ArticleIndex.init()
     es = Elasticsearch()
     from CourseProject.models import Article
     bulk(client=es, actions=(b.indexing() for b in Article.objects.all().iterator()))

def search(name):
    s = Search().filter('term', name=name)
    response = s.execute()
    print(response)

    return response

#################


# from elasticsearch import Elasticsearch
# from elasticsearch.helpers import bulk
# from elasticsearch_dsl.connections import connections
# from elasticsearch_dsl import DocType, Text, Date
#
# from CourseProject.models import Article
# # from django.apps import apps
# # Article = apps.get_model('CourseProject', 'Article')

# connections.create_connection()
#
# class ArticleIndex(DocType):
#     name = Text()
#     creationDate = Date()
#     shortDescription = Text()
#     specialityNumber = Text()
#
#     class Meta:
#         index = 'article-index'
#
# def bulk_indexing():
#     ArticleIndex.init()
#     es = Elasticsearch()
#     bulk(client=es, actions=(b.indexing() for b in Article.objects.all().iterator()))
#
# def search(name):
#     from pip.index import Search
#     s = Search().filter('match', name=name)
#     response = s.execute()
#     return response