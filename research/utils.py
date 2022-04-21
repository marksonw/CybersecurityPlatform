

from .models import Research, Tag
from django.db.models import Q


def searchResearchs(request):
    search_query  = ""

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    tags = Tag.objects.distinct().filter(tag_name__icontains=search_query)    

    researchs = Research.objects.filter(Q(research_title__icontains=search_query) | Q(description__icontains=search_query) | Q(owner__name__icontains=search_query) | Q(tags__in=tags))

    return researchs, search_query