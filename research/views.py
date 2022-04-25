from multiprocessing import context
import profile
from turtle import left
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from research.models import Research
#from django.http import HttpResponse
from .models import Research, Tag
from .forms import ResearchForm
from django.db.models import Q
from .utils import searchResearchs, paginateResearchs

## Researchs Menu Page View Routing 
@login_required(login_url='/')
def researchs(request):
    researchs, search_query = searchResearchs(request)
    custom_range, researchs = paginateResearchs(request, researchs, 3)
  

    context = {'researchs': researchs, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'research/researchs.html', context)

## Research Page
@login_required(login_url='/') 
def research(request, pk):
    researchObj = Research.objects.get(id=pk)
    return render(request, 'research/single-research.html',{'research': researchObj})


## Create Research 
@login_required(login_url='/')
def createResearch(request):
    profile = request.user.profile
    form = ResearchForm()

    ## Create Blog Form Submission
    if request.method == 'POST':
        form = ResearchForm(request.POST, request.FILES)
        if form.is_valid():
            research = form.save(commit=False)
            research.owner = profile
            research.save()
        return redirect('researchs')

    context = {'form': form}
    return render(request, 'research/research-form.html', context)


## Update Research Blog
@login_required(login_url='/')
def updateResearch(request, pk):
    profile = request.user.profile
    research_blog = profile.research_set.get(id=pk)
    form = ResearchForm(instance=research_blog)
    
    ## Update Blog Form Submission
    if request.method == 'POST':
        form = ResearchForm(request.POST, request.FILES, instance=research_blog)
        if form.is_valid():
            form.save()
            return redirect('researchs')

    context = {'form': form}
    return render(request, 'research/research-form.html', context)

## Delete Research Blog
@login_required(login_url='/')
def deleteResearch(request, pk):
    profile = request.user.profile
    research_blog = profile.research_set.get(id=pk)

    ## Delete Blog Submission
    if request.method == "POST":
        research_blog.delete()
        return redirect('researchs')
    context = {'object': research_blog}
    return render(request, 'delete.html', context)