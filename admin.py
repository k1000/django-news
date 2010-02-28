from django.contrib import admin
from models import News, Section
from django.conf import settings

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('headline',)}
    list_display = ('headline', 'pub_date', 'publish')
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'
    exclude = ('author', )
    save_as = True
    
    class Media:
        js = (
            '%s/jquery.wymeditor.pack.js' % settings.WYMEDITOR_PATH,
            '%s/plugins/filebrowser/jquery.wymeditor.filebrowser.js' % settings.WYMEDITOR_PATH,
            '/media/js/admin_wymeditor.js',
        )
        
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

class SectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(Section, SectionAdmin)

