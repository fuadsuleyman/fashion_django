from django.db import models

# Create your models here.

class SubMenu(models.Model):
    # informations
    title = models.CharField('Menu Name', max_length=100, db_index=True)

    # moderations
    status = models.BooleanField('is_active', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sub_menu'
        verbose_name = 'Sub_menu'
        verbose_name_plural = 'Sub_menus'
        ordering = ('-created_at', 'title')

    def __str__(self):
        return self.title 


class FooterInfo(models.Model):
    # informations
    title = models.CharField('Title', max_length=100, db_index=True)
    description = models.TextField('Description', null=True, blank=True)

    # moderations
    status = models.BooleanField('is_active', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'footer_info'
        verbose_name = 'footer_info'
        verbose_name_plural = 'footer_infos'
        ordering = ('-created_at', 'title')

    def __str__(self):
        return self.title 


class FooterSupport(models.Model):
    # informations
    title = models.CharField('Title', max_length=100, db_index=True)

    # moderations
    status = models.BooleanField('is_active', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'footer_support'
        verbose_name = 'Footer_support'
        verbose_name_plural = 'Footer_supports'
        ordering = ('-created_at', 'title')

    def __str__(self):
        return self.title 


class FooterSubscribe(models.Model):
    # informations
    button_text = models.CharField('Title', max_length=100, db_index=True)
    description = models.TextField('Description', null=True, blank=True)

    # moderations
    status = models.BooleanField('is_active', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'footer_subscribe'
        verbose_name = 'Footer_subscribe'
        verbose_name_plural = 'Footer_subscribes'

    def __str__(self):
        return self.button_text 


class FollowUs(models.Model):
    # informations
    title = models.CharField('Title', max_length=100, db_index=True)
    image = models.ImageField('Image', blank=True, upload_to='follow_us')
    facebook_link = models.CharField('facebook', max_length=100, db_index=True)
    insragram_link = models.CharField('instagram', max_length=100, db_index=True)
    image = models.ImageField('face_icon', blank=True, upload_to='follow_us')
    image = models.ImageField('insagram_icon', blank=True, upload_to='follow_us')

    # moderations
    status = models.BooleanField('is_active', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'follow_us'
        verbose_name = 'Follow_us'
        verbose_name_plural = 'Follow_us'

    def __str__(self):
        return self.title 