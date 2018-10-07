from django.shortcuts import render

from django.apps import apps

Article = apps.get_model('CourseProject', 'Article')
Comment = apps.get_model('CourseProject', 'Comment')
Rating = apps.get_model('CourseProject', 'Rating')
Tag = apps.get_model('CourseProject', 'Tag')



def tagSearch(request, id):
    tags = Tag.objects.filter(id__icontains=id)
    data = {"user": request.user,
            "rating": Rating.objects.all(),
            "tags": tags}
    return render(request, 'search/tagSearch.html', context=data)
