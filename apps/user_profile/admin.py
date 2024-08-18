from django.contrib import admin
from .models import Profile, WeightHistory, BodyFatPercentageHistory, MuscleMassHistory

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickName', 'userProfile', 'gender', 'height', 'dateOfBirth', 'created_on')
    search_fields = ('nickName', 'userProfile__email')
    list_filter = ('gender', 'created_on')

class WeightHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'weight', 'date')
    search_fields = ('profile__nickName', 'profile__userProfile__email')
    list_filter = ('date',)
    ordering = ('-date',)  # 最新の記録を先に表示

class BodyFatPercentageHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'bodyFatPercentage', 'date')
    search_fields = ('profile__nickName', 'profile__userProfile__email')
    list_filter = ('date',)
    ordering = ('-date',)

class MuscleMassHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'muscleMass', 'date')
    search_fields = ('profile__nickName', 'profile__userProfile__email')
    list_filter = ('date',)
    ordering = ('-date',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(WeightHistory, WeightHistoryAdmin)
admin.site.register(BodyFatPercentageHistory, BodyFatPercentageHistoryAdmin)
admin.site.register(MuscleMassHistory, MuscleMassHistoryAdmin)