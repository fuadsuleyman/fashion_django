from django.db import models
from account.models import User
from sport_fashion1.utils import unique_slug_generator

# slug yut
from django.db.models.signals import pre_save

# Create your models here.

class Tag(models.Model):

    title = models.CharField('Title', max_length=100, db_index=True)

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tag'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ('-created_at', 'title')

    def __str__(self):
        return self.title


class Marka(models.Model):  
    # adidasin alt marka-lari saxlanilacaq
    
    # informations
    title = models.CharField('Title', max_length=100, db_index=True)
    image = models.ImageField('Image', blank=True, upload_to='marka_images')
    description = models.CharField(max_length=255, blank=True)
    slug = models.SlugField('Slug', max_length=110, unique = True)

    # moderations
    status = models.BooleanField('is_active', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'marka'
        verbose_name = 'Marka'
        verbose_name_plural = 'Markas'
        ordering = ('-created_at', 'title')

    def __str__(self):
        return self.title 


class Sports(models.Model):  
    # idman novleri saxlanilacaq
    
    # informations
    title = models.CharField('Title', max_length=100, db_index=True)
    image = models.ImageField('Image', blank=True, upload_to='sport_images')
    description = models.CharField(max_length=255, blank=True)
    slug = models.SlugField('Slug', max_length=110, unique = True)

    # moderations
    status = models.BooleanField('is_active', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sport'
        verbose_name = 'Sport'
        verbose_name_plural = 'Sports'
        ordering = ('-created_at', 'title')

    def __str__(self):
        return self.title 

class Category(models.Model):

    # relation
    marka = models.ManyToManyField(Marka, related_name='categories')
    sports = models.ManyToManyField(Sports, related_name='categories')
    parent = models.ManyToManyField('self', related_name='children', blank=True)

    # information
    title = models.CharField('Title', max_length=100, db_index=True)
    image = models.ImageField('Image', blank=True, upload_to='categories_images')
    description = models.CharField(max_length=255, blank=True)
    slug = models.SlugField('Slug', max_length=110, unique = True)
    is_main = models.BooleanField('is_main', default=False)
    is_second = models.BooleanField('is_second', default=False)
    is_third = models.BooleanField('is_third', default=False)

    # moderations
    status = models.BooleanField('is_active', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('-created_at', 'title')
        unique_together = ('slug',)

    def __str__(self):
        return self.title


class Product(models.Model):
    """
    very important table
    """
    # relations
    tags = models.ManyToManyField(Tag, related_name='products')
    same_product = models.ManyToManyField('self', related_name='same_products', blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='product_categories')
    who_like = models.ManyToManyField(User, related_name='liked_products', blank=True)

    # informations
    color_title = models.CharField('Color Name', max_length=50, blank=True, null=True)
    color_code = models.CharField('Color code', max_length=50, blank=True, null=True)
    title = models.CharField('Title', max_length=100, db_index=True)
    slug = models.SlugField('Slug', max_length=110, unique = True, blank=True)
    sku = models.CharField('SKU', max_length=50, db_index=True)
    description = models.TextField('Description', null=True, blank=True)
    sale_count = models.IntegerField('Sale Count', default=0)
    is_new = models.BooleanField('is_new', default=True)
    is_featured = models.BooleanField('is_featured', default=False)
    is_discount = models.BooleanField('is_discount', default=False)

    # price info
    CHOICES = (
        (1, 'Not'),
        (2, 'Percent'),
        (3, 'Unit'),
    )
    price = models.DecimalField('Price', max_digits=7, decimal_places=2)
    discount_type = models.PositiveIntegerField("Discount Type", choices=CHOICES, default=1)
    discount_value = models.IntegerField('Discount Value', null=True, blank=True)

    # moderations
    status = models.BooleanField('is_active', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('title', 'slug')
        # slug unique
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('-created_at', 'title')
    

    def get_price(self):
        if self.discount_type == 1:
            return self.price
        elif self.discount_type == 2:
            return self.price - (self.price * self.discount_value / 100)
        else:
            return self.price - self.discount_value
    
    def get_is_discount(self):
        if self.get_price() < self.price:
             is_discount = True
    
    def get_is_new(self):
        delta = datetime.now().date() - self.created_at
        if delta.days <= 30:
             is_new = True

    def __str__(self):
        return f'{self.title} {self.color_title}'

# slug 
def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

# herdefe Product-un instance-i yarandiqda asagidaki funqsiya ishe dushur
pre_save.connect(slug_generator, sender=Product)
# pre_save.connect(slug_generator, sender=Category)


class Product_images(models.Model):
    # product-un butun sekilleri burda saxlanacaq
    # is_main true olan esas shekildi
    # is_second_main olan shekil coxlu product sehifesinde hover edende gelen sekildi

    # relations
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    # informations
    image = models.ImageField('Image', upload_to='product_images')
    is_main = models.BooleanField('Main Image', default=False) 
    is_second_main = models.BooleanField('Second Main Image', default=False) 

    # moderations
    status = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'image'
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.image}'


class Product_sizes(models.Model):
    # ayaqqabi ve ya geyimiz olculerini saxlayir

    # relations
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sizes')

    # informations
    size = models.CharField('Title', max_length=100, db_index=True)
    relation = models.ManyToManyField(Product, through='Product_sizes_rel')
    

    # moderations
    status = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_sizes'
        verbose_name = 'Product_sizes'
        verbose_name_plural = 'Product_sizes'
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.size}'


class Product_sizes_rel(models.Model):
    # relations
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products_rel')
    product_sizes = models.ForeignKey(Product_sizes, on_delete=models.CASCADE, related_name='sizes_rel')

    # informations
    in_stock = models.IntegerField('In Stock')


    def __str__(self):
        return str(self.in_stock)
    


class Product_futures(models.Model):
    # product-un detail melumatlerinin adlarini ve iceri melumatlarini saxlayir
    
    # relations
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='futures')

    # informations
    title = models.CharField('Title', max_length=50, db_index=True)
    content = models.TextField('Detail Content', null=True, blank=True)

    # moderations
    status = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_futures'
        verbose_name = 'Product_futures'
        verbose_name_plural = 'Product_futures'
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.title}'


class Product_colors(models.Model):
    # eyni bir product bir nece renge sahib ola bildiyi ucun yaratdim    
    # relations
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='colors')

    # informations
    # coler_title = models.CharField('Title', max_length=50, db_index=True, blank=True, null=True)
    # color_code = models.CharField('Title', max_length=50, db_index=True, blank=True, null=True)

    # moderations
    status = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_colors'
        verbose_name = 'Product_color'
        verbose_name_plural = 'Product_colors'
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.title}'




