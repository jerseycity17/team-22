import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ishar.settings")
django.setup()

from isharonline.models import meditations
import json

def landingtop10():
    top10 = meditations.objects.all().order_by('-PublicationYear')[:10]

    cache = {}

    category = ['Key','ItemType','PublicationYear','Author','Title','PublicationTitle','ISBN','ISSN','DOI','Url','AbstractNote','Date',
                'DateAdded','DateModified','AccessDate','Pages','NumPages','Issue','Volume','NumberOfVolumes','JournalAbbreviation',
                'ShortTitle','Series','SeriesNumber','SeriesText','SeriesTitle','Publisher','Place','Language','Rights','Type',
                'Archive','ArchiveLocation','LibraryCatalog','CallNumber','Extra','Notes','FileAttachments','LinkAttachments',
                'ManualTags','AutomaticTags','Editor','SeriesEditor','Translator','Contributor','AttorneyAgent','BookAuthor',
                'CastMember','Commenter','Composer','Cosponsor','Counsel','Interviewer','Producer','Recipient','ReviewedAuthor',
                'Scriptwriter','WordsBy','Guest','Number','Edition','RunningTime','Scale','Medium','ArtworkSize','FilingDate',
                'ApplicationNumber','Assignee','IssuingAuthority','Country','MeetingName','ConferenceName','Court','References',
                'Reporter','LegalStatus','PriorityNumbers','ProgrammingLanguage','Version','System','Code','CodeNumber','Section',
                'Session','Committee','History','LegislativeBody']

    for i, v in enumerate(top10):
        fields = str(v).split("|")
        print(fields)
        cache_tmp = {}
        for j, f in enumerate(fields):
            cache_tmp[category[j]] = f
        cache[i + 1] = cache_tmp

    return json.dumps(cache)
