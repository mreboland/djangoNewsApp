from django.contrib import admin
from .models import Article, Comment


# If we want to be able to see every comment associated with each post we can do so using a django admin feature called inlines which displays foreignKey relationships in a nice way.
# There are two main inline views used, TabularInline, and StackedInline. In a TabularInline all model fields appear on one line while in a StackedInline each field has its own line.

# StackedInLine
# class CommentInLine(admin.StackedInline):
#     model = Comment
    # If we want to limit the display of empty rows (defaults 3) we do:
    # extra = 0
    
# class ArticleAdmin(admin.ModelAdmin):
#     inlines = [
#         CommentInLine,
#     ]
    
# TabularInLine
class CommentInline(admin.TabularInline):
    model = Comment
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
