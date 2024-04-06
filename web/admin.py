from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from . models import Banner,Services,ClientLogos,ServiceDescription,Blog,BlogDescription,Testimonial

# Register your models here.
@admin.register(Banner)
class BanerAdmin(ImportExportActionModelAdmin):
    list_display = ("title","background_image","is_active",)
    search_fields = ("title",)

class ServiceDescriptionInline(admin.TabularInline):
    model = ServiceDescription
    extra = 1

@admin.register(Services)
class ServicesAdmin(ImportExportActionModelAdmin):
    list_display = ("title","description", "background_image","is_active",)
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ServiceDescriptionInline]

@admin.register(ClientLogos)
class ClientLogosAdmin(admin.ModelAdmin):
    list_display = (
        "logo",
    )

class BlogDescriptionInline(admin.TabularInline):
    model = BlogDescription
    extra = 1

@admin.register(Blog)
class BlogAdmin(ImportExportActionModelAdmin):
    list_display = ("title","description", "thumbnail_img","is_active",)
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [BlogDescriptionInline]

@admin.register(Testimonial)
class TestimonialAdmin(ImportExportActionModelAdmin):
    list_display = ("name","profile_image","is_active",)
    search_fields = ("name",)