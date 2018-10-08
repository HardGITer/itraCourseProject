# from django_elasticsearch_dsl import DocType, Index
# from CourseProject.models import Article
# # from django.apps import apps
#
# # Article = apps.get_model('CourseProject', 'Article')
#
# articles = Index('articles')
#
# @articles.doc_type
# class ArticleDocument(DocType):
#     class Meta:
#         model = Article
#
#         fields = [
#             'name',
#             'shortDescription',
#             'mainText',
#             'creationDate',
#             'id',
#         ]
