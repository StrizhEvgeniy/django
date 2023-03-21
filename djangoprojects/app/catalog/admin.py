from django.contrib import admin
from .models import Book,Author,Genre,Language,BookInstance


admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Book)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status','due_back','id','borrower')
    list_filter = ('status','due_back')

    fieldsets = (
        (None,{
            'fields':('book','id')
        }),
        ('Availability',{
            'fields': ('status','due_back','borrower')
        })
    )

