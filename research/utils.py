
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Research, Tag
from django.db.models import Q


def searchResearchs(request):
    search_query  = ""

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    tags = Tag.objects.distinct().filter(tag_name__icontains=search_query)    

    researchs = Research.objects.filter(Q(research_title__icontains=search_query) | Q(description__icontains=search_query) | Q(owner__name__icontains=search_query) | Q(tags__in=tags))

    return researchs, search_query


def paginateResearchs(request, researchs, results):
    page = request.GET.get('page')
    paginator = Paginator(researchs, results)

    try:
        researchs = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        researchs = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        researchs = paginator.page(page)
    
    left_index = (int(page) - 4)

    if left_index < 1:
        left_index = 1

    right_index = (int(page) + 5)

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1
    
    custom_range = range(left_index, right_index)

    return custom_range, researchs
