from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from .models import User

class UserAdmin(BaseUserAdmin):
    # 管理画面に表示されるフィールド
    list_display = ('id', 'email', 'uid', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('email', 'uid')
    ordering = ('email',)

    # フィールドセット: ユーザー詳細画面のフィールド構成
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('uid',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # 新規ユーザー作成画面のフィールド構成
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'uid', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

admin.site.register(User, UserAdmin)