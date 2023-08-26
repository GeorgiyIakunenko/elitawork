from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin
from django.contrib.auth.models import Group
from .models import Position, Manager, Contact, MessengerPlatform


def manager_through_str(self):
    return f"{self.manager.name}"


Manager.positions.through.__str__ = manager_through_str


class ManagerInline(admin.TabularInline):
    model = Manager.positions.through
    extra = 1
    verbose_name = "Менеджер для этой позиции"
    verbose_name_plural = "Менеджеры для этой позиции"


class PositionAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("name", "important", "get_picture_small", "position_order")
    list_display_links = ("name",)
    list_editable = ("important",)
    readonly_fields = ('get_picture_large',)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ManagerInline]

    def get_picture_small(self, obj):
        return mark_safe(f'<img src={obj.picture.url} width=150px')

    get_picture_small.short_description = "Превью"

    def get_picture_large(self, obj):
        return mark_safe(f'<img src={obj.picture.url} width=250px')

    get_picture_large.short_description = "Пример"

    def add_view(self, request, extra_content=None):
        self.fields = ("name", "slug", "important", "salary", "location", "note", "short_description", "description", "picture")
        return super().add_view(request)

    def change_view(self, request, object_id, extra_context=None):
        self.fieldsets = (
            (None,
             {
                 'fields': ('name', 'slug', 'important', 'salary', 'location', 'note', 'short_description', 'description')
             }
             ),
            (None,
             {
                 'fields': (('picture', 'get_picture_large'),)
             })
        )
        return super().change_view(request, object_id)


class MessengerPlatformInline(admin.TabularInline):
    model = Contact.messenger_platforms.through
    extra = 1


def contact_through_str(self):
    return "Номер"


Manager.contacts.through.__str__ = contact_through_str


class ContactInline(admin.TabularInline):
    model = Manager.contacts.through
    extra = 1
    inlines = [MessengerPlatformInline]
    verbose_name = "Контакт"
    verbose_name_plural = "Контакты"


class ManagerAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("name", "get_photo_small", "manager_order")
    list_display_links = ("name",)
    readonly_fields = ('get_photo_large',)
    inlines = [ContactInline]

    def get_photo_small(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width=150px')

    get_photo_small.short_description = "Превью"

    def get_photo_large(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width=250px')

    get_photo_large.short_description = "Пример"

    def add_view(self, request, extra_content=None):
        self.fields = ("name", "job_position", "positions", "photo")
        return super().add_view(request)

    def change_view(self, request, object_id, extra_context=None):
        self.fieldsets = (
            (None,
             {
                 'fields': ("name", "job_position", "positions")
             }
             ),
            (None,
             {
                 'fields': (('photo', 'get_photo_large'),)
             })
        )
        return super().change_view(request, object_id)


class MessengerPlatformAdmin(admin.ModelAdmin):
    list_display = ("name", "get_logo")
    list_display_links = ("name",)
    readonly_fields = ('get_logo',)

    def get_logo(self, obj):
        return mark_safe(f'<img src={obj.logo.url} width=50px')

    get_logo.short_description = "Logo"


admin.site.register(Position, PositionAdmin)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(Contact)
admin.site.register(MessengerPlatform, MessengerPlatformAdmin)

admin.site.unregister(Group)


admin.site.site_title = "Elita Work Admin"
admin.site.site_header = "Elita Work Admin"
