from django_elasticsearch_dsl import DocType, Index
from mysite.CourseProject.models import Article

articles = Index('articles')


@articles.doc_type
class ArticleDocument(DocType):
    class Meta:
        model = Article

        fields = [
            'name',
            'shortDescription',
            'mainText',
            'creationDate',
            'id',
        ]