from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    class BookAdmin(admin.ModelAdmin):
        list_display = ('title', 'author', 'publication_year')
        search_fields = ('title', 'author')
        list_filter = ('author', 'publication_year')

admin.site.register(Book, BookAdmin)

class UserAdmin(BaseUserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'date_of_birth', 'profile_photo'),
        }),
    )
    list_display = ('username', 'first_name', 'last_name', 'date_of_birth', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(CustomUser, UserAdmin)