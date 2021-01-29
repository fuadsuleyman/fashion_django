from django.contrib import admin
from django.urls import path, include

# below 2 lines for image
from django.conf import settings
from django.conf.urls.static import static

from index import views as index_views
from product import views as product_views
# from contact import views as contact_views

admin.site.site_header = 'Sport Fashion admin'
admin.site.site_title = 'Sport Fashion admin'
admin.site.index_title = 'Sport Fashion administration'

urlpatterns = [
    path('api/', include('api.urls')),
    path('', include('index.urls')),
    path('', include('order.urls')),
    path('', include('account.urls')),
    path('', include('product.urls')),
    path('', include('contact.urls')),
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
