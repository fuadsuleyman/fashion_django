from django.contrib import admin

# Register your models here.

from .models import SubMenu, FooterInfo, FooterSupport, FooterSubscribe, FollowUs 

admin.site.register(SubMenu)
admin.site.register(FooterInfo)
admin.site.register(FooterSupport)
admin.site.register(FooterSubscribe)
admin.site.register(FollowUs)
