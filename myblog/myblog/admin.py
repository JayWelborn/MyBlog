from django.contrib import admin

from blog.models import Category, Entry
from polls.models import Question, Choice
from home.models import About, Contact


# Add blog categories
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


# Add blog entries
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


# add about me page
class AboutMe(admin.ModelAdmin):
    """
    TODO
    """


class ContactMe(admin.ModelAdmin):
    """
    TODO
    """


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


# Customizes header on admin site
class MyAdminSite(admin.AdminSite):
    site_header = 'JDevelops Administration'


blog_admin = MyAdminSite(name='admin')
blog_admin.register(Category, CategoryAdmin)
blog_admin.register(Entry, BlogAdmin)
blog_admin.register(Question, QuestionAdmin)
blog_admin.register(About)
blog_admin.register(Contact)
