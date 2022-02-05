from django.shortcuts import render
#from django.http import HttpResponse


projectsList = [
    {
        "id": "1",
        "title": "First Project",
        "description": "This is the first project",
    },

    {
        "id": "2",
        "title": "Second Project",
        "description": "This is the second project",
    },

    {
        "id": "3",
        "title": "Third Project",
        "description": "This is the third project",
    },
]

# Create your views here.
def research(request):
    msg = "Hello this is the message!"
    number = 10
    context = {"msg": msg, "number":number, "projects":projectsList}
    return render(request, 'research/research.html', context)
