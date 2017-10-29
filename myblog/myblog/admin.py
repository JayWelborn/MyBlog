from django.contrib import admin

from blog.models import Tag, Entry
from polls.models import Question, Choice
from home.models import About, Contact, FunFact, BrandInfo
from bingo.models import BingoBlock, BingoCard, FreeSpace


# Add blog entries
class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title', 'slug']}),
        ('Publication Date', {'fields': ['pub_date']}),
        ('Header', {'fields': ['header_image']}),
        ('Entry', {'fields': ['body', 'tags']}),
    ]
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']


# Add choices to Polls DB
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


# Add Questions to Polls DB
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question',         {'fields': ['question_text']}),
        ('Publication Date', {'fields': ['pub_date']})
    ]

    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


class BingoBlockInline(admin.TabularInline):
    model = BingoBlock
    extra = 24
    max_num = 30


class FreeSpaceInline(admin.TabularInline):
    model = FreeSpace
    extra = 1
    max_num = 1


class BingoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title', 'slug']}),
        ('Publication Date', {'fields': ['pub_date']}),
        ('Optional Media', {'fields': ['header_image', 'victory_song']})
    ]
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']
    inlines = [BingoBlockInline, FreeSpaceInline]


# Customizes header on admin site
class MyAdminSite(admin.AdminSite):
    site_header = 'Jay Welborn Administration'


blog_admin = MyAdminSite(name='admin')
blog_admin.register(Entry, BlogAdmin)
blog_admin.register(Tag)
blog_admin.register(Question, QuestionAdmin)
blog_admin.register(About)
blog_admin.register(Contact)
blog_admin.register(FunFact)
blog_admin.register(BrandInfo)
blog_admin.register(BingoCard, BingoAdmin)
