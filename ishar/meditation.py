import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ishar.settings")
django.setup()

from isharonline.models import meditations

all_entries = meditations.objects.all()
print(all_entries)
