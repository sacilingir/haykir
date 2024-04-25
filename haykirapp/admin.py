from django.contrib import admin
from haykirapp.models import Tweet

class TweetAdmin(admin.ModelAdmin):
    fields = ['message','nickname']


admin.site.register(Tweet,TweetAdmin)