from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from research.models import Research
#from django.http import HttpResponse
from .models import Research
from .forms import ResearchForm


## Researchs Menu Page View Routing 
@login_required(login_url='/')
def researchs(request):
    researchs = Research.objects.all()
    context = {'researchs': researchs}
    return render(request, 'research/researchs.html', context)

## Research Page
@login_required(login_url='/') 
def research(request, pk):
    researchObj = Research.objects.get(id=pk)
    return render(request, 'research/single-research.html',{'research': researchObj})


## Create Research 
@login_required(login_url='/')
def createResearch(request):
    form = ResearchForm()

    ## Create Blog Form Submission
    if request.method == 'POST':
        form = ResearchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('researchs')

    context = {'form': form}
    return render(request, 'research/research-form.html', context)


## Update Research Blog
@login_required(login_url='/')
def updateResearch(request, pk):
    research_blog = Research.objects.get(id=pk)
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
    research_blog = Research.objects.get(id=pk)

    ## Delete Blog Submission
    if request.method == "POST":
        research_blog.delete()
        return redirect('researchs')
    context = {'object': research_blog}
    return render(request, 'research/delete.html', context)