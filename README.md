## JBD 5th sprint project: E-commerce

### 2.day tasks

1. Məhsul səhifəsini dinamik hala gətirin. Ana səhifə və ya çoxlu məhsul səhifəsində məhsula kliklədikdə. Həmin məhsul açılmalıdır.
2. Ana səhifə, çoxlu məhsul səhifələri və məhsul səhifəsinin əksikləri tamamlanmalıdır.



## JBD 7th sprint project: Rest Api

### 2.day tasks

* Bu günün tasklarında Django Rest Framework istifadə edilərək məhsullar üçün api yazılacaq.

1. Proyektinizə restframework install edin və qurun. (https://www.django-rest-framework.org/tutorial/quickstart/) / done
2. Product app-inin daxilində api folderi yaradın. / done
3. Daxilində serializers.py, urls.py, views.py faylları olsun. / done
4. serializers.py faylının daxilində Product modeli üçün serializer düzəldin. / done
5. product/api/views.py faylında @api_view dekoratoru istifadə olunaraq 5 funksiya yazılmalıdır. (all_products, get_product, create_product, update_product, delete_product) / done
6. all_products funksiyası bütün məhsulların listini qaytarmalıdır. / done
7. get_product funksiyası verilən id-yə uyğun məhsulun məlumatlarını qaytarmalıdır. / done
8. create_product funksiyası daxilində göndərilən məlumatlara uyğun məhsul yaratmalıdır. / done
9. update_product funksiyası verilən id-yə uyğun məhsulun qiymətini dəyişməlidir. (yeni qiymət price key-i ilə sorğunun datasında göndəriləcək) / 
10. delete_product funksiyası verilən id-yə uyğun məhsulu silməlidir. / done
11. product/api/urls.py faylında yuxarıdakı funksiyalar üçün path-lər yazılmalıdır. /done
12. Proyektin əsas urls-ində qeyd edilməlidir ki, /api/v1/products url-inə müraciət olunanda sorğu product/api/urls.py-a yönləndirilsin. / done
13. Yazdığınız api-ləri Postman vasitəsi ilə test edin. / done
