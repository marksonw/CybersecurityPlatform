from .models import Profile, Interests
from django.db.models import Q

def searchProfiles(request):
    search_query  = ""

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")
    
    interests = Interests.objects.filter(name__icontains=search_query)
    profiles = Profile.objects.distinct().filter(Q(name__icontains=search_query) | Q(bio__icontains=search_query) | Q(username__icontains=search_query) | Q(name__in=interests))

    return profiles, search_query, interests
