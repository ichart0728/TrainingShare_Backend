from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    # 管理画面に表示されるフィールド
    list_display = ('id', 'nickName', 'userProfile', 'gender', 'height', 'dateOfBirth', 'created_on')
    list_filter = ('gender', 'created_on')
    search_fields = ('nickName', 'userProfile__email')
    ordering = ('created_on',)

    # フィールドセット: プロフィール詳細画面のフィールド構成
    fieldsets = (
        (None, {'fields': ('nickName', 'userProfile')}),
        ('Personal info', {'fields': ('gender', 'height', 'dateOfBirth')}),
        ('Important dates', {'fields': ('created_on',)}),
    )

    # read-only フィールド
    readonly_fields = ('created_on',)

admin.site.register(Profile, ProfileAdmin)