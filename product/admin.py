from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import Tag, Marka, Sports, Category, Product, Product_images, Product_sizes, Product_futures, Product_colors, Product_sizes_rel

class ImageInline(admin.TabularInline):
    model = Product_images
    extra = 0

# class SizeInline(admin.TabularInline):
#     model = Product_sizes
#     extra = 0

# class ColorInline(admin.TabularInline):
#     model = Product_colors
#     extra = 0

class FuturesInline(admin.StackedInline):
    model = Product_futures
    extra = 0

class ProductSizesInline(admin.StackedInline):
    model = Product_sizes
    extra = 0

class ProductSizesRelInline(admin.StackedInline):
    model = Product_sizes_rel
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'color_title', 'is_new', 'is_featured', 'is_discount', 'status')
    list_display_links = ("title",)
    list_filter = ('status', 'created_at')
    search_fields = ('title', ) # owner elave edende error verir
    # prepopulated_fields = {'slug': ('title', )}
    inlines = [ImageInline, ProductSizesRelInline, FuturesInline]
    lest_per_page = 20
    save_on_top = True
    save_as = True #create new product easy way
    actions = ('update_product_status', )
    # fields = ('owner', 'category', ('title', 'slug'), 'short_description', 'description', 'image', 'tags', 'is_published')
    fieldsets = (
        ('Relations', {
            'fields': ('category', 'tags', 'same_product', 'who_like'),
        }),
        ('Informations', {
            'fields': (('title', 'slug'), 'sku', 'color_title', 'color_code', 'description', 'sale_count', 'is_new', 'is_featured', 'is_discount', 'status')
        }),
        ('Price Info', {
            'fields': ('price', 'discount_type', 'discount_value'),
        }),
    )
    
    def update_product_status(self, request, queryset):
        count = queryset.update(is_published=False) #  beraberden sonra not is_published 
        self.message_user(request, f'{count} products status are updated')
    
    # def get_image(self, obj):   
    #     # product.images.get(is_main=True).image.url
    #     return mark_safe(f'<img src={obj.objects.filter(is_main=True).image.url} width="50" height="60"')
        
    update_product_status.short_description = 'Update selected recipes is published status'
    # get_image.short_description = "Image"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent_category' ,'is_main', 'is_second', 'is_third', 'status')
    list_display_links = ("title",)
    save_on_top = True
    save_as = True #create new product easy way
    fieldsets = (
        ('Relations', {
            'fields': ('marka', 'sports', 'parent'),
        }),
        ('Informations', {
            'fields': (('title', 'slug'), 'image', 'description', 'is_main', 'is_second', 'is_third')
        }),
    )

    def parent_category(self, obj):
        if obj.parent:
            return obj.parent


admin.site.register(Tag)
admin.site.register(Marka)
admin.site.register(Sports)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Product_images)
admin.site.register(Product_sizes)
admin.site.register(Product_futures)
admin.site.register(Product_colors)
admin.site.register(Product_sizes_rel)