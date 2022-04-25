from .models import Profile, Interests
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def searchProfiles(request):
    search_query  = ""

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")
    
    interests = Interests.objects.filter(name__icontains=search_query)
    profiles = Profile.objects.distinct().filter(Q(name__icontains=search_query) | Q(bio__icontains=search_query) | Q(username__icontains=search_query) | Q(name__in=interests))

    return profiles, search_query, interests

def paginateProfiles(request, profiles, results):
    page = request.GET.get('page')
    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)
    
    left_index = (int(page) - 4)

    if left_index < 1:
        left_index = 1

    right_index = (int(page) + 5)

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1
    
    custom_range = range(left_index, right_index)

    return custom_range, profiles
