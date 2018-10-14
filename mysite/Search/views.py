from django.shortcuts import render
# from Search.documents import ArticleDocument
from django.apps import apps
from elasticsearch_dsl import DocType, Text, Date, Search
Rating = apps.get_model('CourseProject', 'Rating')
Tag = apps.get_model('CourseProject', 'Tag')

def tagSearch(request, id):
    tags = Tag.objects.filter(id__icontains=id)
    data = {"user": request.user,
            "rating": Rating.objects.all(),
            "tags": tags}
    return render(request, 'search/tagSearch.html', context=data)

def absoluteSearch(request):
    s = Search().filter('term', name=request.GET.get('q'))
    response = s.execute()
    return render(request, 'search/search.html', { "articles": response, "user": request.user, "rating": Rating.objects.all() })


# def search(name):
#     s = Search().filter('term', name=name)
#     response = s.execute()
#     print(response[0].mainText)
#
#     return response

# def search(request):
#     from Search.search import ArticleIndex
#     posts = ArticleIndex.search().query("match", title="test")
#
#     return posts.execute()


#     q = request.GET.get('q')
#     # if q:
#     articles = ArticleDocument.search().query("match", title=q)
#     # else:
#     #     articles = ''
#
#     return render(request, 'search/search.html', {"articles": articles})