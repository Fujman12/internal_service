from django.contrib import admin
from .models import IdentifierType, Classification, Watchlist, WatchlistItem

admin.site.register(IdentifierType)
admin.site.register(Classification)
admin.site.register(Watchlist)
admin.site.register(WatchlistItem)
