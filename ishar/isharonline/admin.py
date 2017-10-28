from django.contrib import admin

# Register your models here.
from .models import Ishar
from .models import meditations

admin.site.register(Ishar)
admin.site.register(meditations)
