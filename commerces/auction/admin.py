from django.contrib import admin
from .models import User, listing, comment, bids
# Register your models here.

admin.site.register(User)
admin.site.register(listing)
admin.site.register(comment)
admin.site.register(bids)
