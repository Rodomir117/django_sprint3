from django.contrib import admin

from .models import Category, Location, Post


class PostAdmin(admin.ModelAdmin):
    list_filter = ('category', 'location')
    ordering = ('title',)
    search_fields = ('title',)


class PostInline(admin.TabularInline):
    model = Post
    extra = 0
    ordering = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    inlines = (PostInline,)
    list_filter = ('posts',)
    ordering = ('title',)


class LocationAdmin(admin.ModelAdmin):
    inlines = (PostInline,)
    list_filter = ('posts',)
    ordering = ('name',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)

admin.site.empty_value_display = 'Не задано'
