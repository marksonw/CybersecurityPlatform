from multiprocessing import context
from django.shortcuts import render

from research.models import Research
#from django.http import HttpResponse
from .models import Research
from .forms import ResearchForm



def researchs(request):
    researchs = Research.objects.all()
    context = {'researchs': researchs}
    return render(request, 'research/researchs.html', context)

def research(request, pk):
    researchObj = Research.objects.get(id=pk)
    return render(request, 'research/single-research.html',{'research': researchObj})


def createResearch(request):
    form = ResearchForm()
    context = {'form': form}
    return render(request, 'research/research-form.html', context)