from django.conf.urls import url

from . import views as product_views


urlpatterns = [
    # ex: /dashboard/
    url(r'^$', product_views.index),

    # ex: /dashboard/product/
    url(r'^product/$', product_views.product_list, name='products'),

    # ex: /dashboard/product/new
    url(r'^product/new/$', product_views.product_create, name='new-product'),

    # ex: /dashboard/product/3/
    url(
        r'^product/(?P<pk>[0-9]+)/$',
        product_views.product_detail,
        name='product',
    ),

    # ex: /dashboard/article/
    url(r'^article/$', product_views.article_list, name='articles'),

    # ex: /dashboard/article/new
    url(r'^article/new/$', product_views.article_create, name='new-article'),

    # ex: /dashboard/article/3/
    url(
        r'^article/(?P<pk>[0-9]+)/$',
        product_views.article_detail,
        name='article',
    ),

    # ex: /dashboard/rental/
    url(r'^rental/$', product_views.rental_list, name='rentals'),

    # ex: /dashboard/rental/new
    url(r'^rental/new/$', product_views.rental_create, name='new-rental'),

    # ex: /dashboard/rental/5/
    url(
        r'^rental/(?P<pk>[0-9]+)/$',
        product_views.rental_detail,
        name='rental',
    ),
]