from django.contrib import admin
from unesco.models import States,Region,Site,Iso,Category
# Register your models here.

admin.site.register(Site)
admin.site.register(Category)
admin.site.register(States)
admin.site.register(Iso)
admin.site.register(Region)