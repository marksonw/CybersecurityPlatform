import imp
from django.contrib import admin

# Register your models here.

from.models import Research
from.models import Feedback
from.models import Tag

admin.site.register(Research)
admin.site.register(Feedback)
admin.site.register(Tag)