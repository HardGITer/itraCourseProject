from django.shortcuts import render
# from Search.documents import ArticleDocument
from django.apps import apps
#
# Article = apps.get_model('CourseProject', 'Article')
# Comment = apps.get_model('CourseProject', 'Comment')
Rating = apps.get_model('CourseProject', 'Rating')
Tag = apps.get_model('CourseProject', 'Tag')

def tagSearch(request, id):
    tags = Tag.objects.filter(id__icontains=id)
    data = {"user": request.user,
            "rating": Rating.objects.all(),
            "tags": tags}
    return render(request, 'search/tagSearch.html', context=data)


# def absoluteSearch(request):
#     q = request.GET.get('q')
#     # if q:
#     articles = ArticleDocument.search().query("match", title=q)
#     # else:
#     #     articles = ''
#
#     return render(request, 'search/search.html', {"articles": articles})