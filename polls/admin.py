from django.contrib import admin

from .models import Question, Choice


# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fieldsets 元组中的第一个元素是字段集的标题
    fieldsets = [
        ('Question content', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # 这会告诉 Django：“Choice 对象要在 Question 后台页面编辑。默认提供 3 个足够的选项字段"
    inlines = [ChoiceInline]

    # 添加了一个“过滤器”侧边栏，允许人们以 pub_date 字段来过滤列表：
    list_filter = ['pub_date']

    # 显示哪几个？
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # 在列表的顶部增加一个搜索框。当输入待搜项时，Django 将搜索 question_text 字段
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
