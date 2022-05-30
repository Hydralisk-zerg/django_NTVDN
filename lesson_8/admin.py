from django.contrib import admin
from lesson_8.models import GamerLibraryModel, GamerModel, GameModel

admin.site.register(GamerLibraryModel)
admin.site.register(GameModel)
admin.site.register(GamerModel)
