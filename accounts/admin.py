from django.contrib import admin
from accounts.models import Post
from accounts.models import Profile

# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)

