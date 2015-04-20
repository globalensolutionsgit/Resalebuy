
from django.conf import settings
from django.conf.urls import patterns, include, url
from adjod.views import *
from advertisement.views import *
from paypal_integration.views import *
from advertisement.forms import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from haystack.views import SearchView, FacetedSearchView
from advertisement.models import Product
from advertisement.searchform import ProductSearchFilter
from advertisement.fixido_search import AdjodSearchView, AdjodSearchViewCategory
# from advertisement.fixido_search import AdjodSearchView

from django.template.loader import add_to_builtins
add_to_builtins('advertisement.templatetags.app_filters')

admin.autodiscover()
# from rest_framework import routers
# from services.views import MessageViewSet
# 
# router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'message', MessageViewSet)


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'adjod.views.home', name='home'),
    # url(r'^adjod/', include('adjod.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^home/$', 'adjod.views.home', name='home'),
    
    url(r'^postad/$', 'advertisement.views.product_form',name='product_form'),

    # url(r'^search/$', 'advertisement.views.search', name='search'),
    # url(r'^search/$', 'advertisement.views.search', name='search'),
    url(r'^postad/(?P<name>.*)/$', 'advertisement.views.sub_category',name='category_name'),

    url(r'^login/$', 'adjod.views.user_login', name='user_login'),
    url(r'^start/$', 'adjod.views.start',name='start'),
    url(r'^new_user/$', 'adjod.views.register', name='register'),
    url(r'^confirm/(?P<confirmation_code>.*)/(?P<username>.*)/', 'adjod.views.confirm',name='confirm' ),
   
    url(r'^ads/(?P<pk>\d+)/$', 'advertisement.views.product_detail',name='product_detail'),
    url(r'^addproduct/$', 'advertisement.views.product_save',name='product_save'),
    url(r'^paypal/$', 'adjod.views.view_that_asks_for_money', name='paypal'),
    url(r'^something/paypal/$', include('paypal.standard.ipn.urls')),
    url(r'^localities_for_city/$','advertisement.views.localities_for_city', name='localities_for_city'),
    url(r'^models_for_brand/$','advertisement.views.models_for_brand', name='models_for_brand'),
        
    url(r'^logout/$', 'adjod.views.logout_view', name='logout_view'),

    # url(r'^v3/postad/$', 'advertisement.views.post_ad_v3', name='post_ad_v3'),
    url(r'^v2/postad/$', 'advertisement.views.post_ad_v2', name='post_ad_v2'),
    url(r'^v3/addetail/$', 'advertisement.views.ad_detail_v3', name='ad_detail_v3'),
    # url(r'^v3/postad/$', 'advertisement.views.product_form_v3', name='product_form_v3'),
    url(r'^subcategory_for_category/$', 'advertisement.views.subcategory_for_category',name='subcategory'),
    url(r'^brand_for_subcategory/$', 'advertisement.views.brand_for_subcategory',name='brand'),
    
    url(r'^postad/$', 'advertisement.views.post_ad1',name='postad'),
    url(r'^sample/$', 'advertisement.views.sample',name='sample'),
#     url(r'^api/',include(router.urls)),
#     url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),

   
    
    # # url(r'^userpage/$', 'adjod.views.user_page',name='userpage'),
    # # url(r'^start/(?P<user_id>\d+)/$', 'adjod.views.start',name='start'),

    # url(r'^start/$', 'adjod.views.start',name='start'),
    

  
    # url(r'^postpage/$', 'advertisement.views.post_page',name='post_page'),
    # url(r'^addproduct/$', 'advertisement.views.product_save',name='product_save'),
    
    
    
    # url(r'^categorypage/$', 'advertisement.views.category_page',name='category_page'),
    # url(r'^postad/(?P<subid>\d+)$', 'advertisement.views.product_form',name='product_form'),

    # url(r'^(?i)(?P<categoryname>.*)/(?P<subcategoryname>.*)/', 'advertisement.views.sub_category_ads', name='sub_category_ads'),


    url(r'^(?i)search/', AdjodSearchView(
      template='advertisement/quikr_search_v2.html', 
      form_class=ProductSearchFilter, 
      # results_per_page=settings.SEARCH_PAGE_NUMBER_OF_LEADS
    ), name='searchPageV2'),


    url(r'^(?i)(?P<categoryname>.*)/(?P<subcategoryname>.*)/', AdjodSearchViewCategory(
      template='advertisement/quikr_search_v2.html', 
      form_class=ProductSearchFilter, 
      # results_per_page=settings.SEARCH_PAGE_NUMBER_OF_LEADS
    ), name='searchPageV2'),
    
    # url(r'^(?P<pk>\d+)/', 'advertisement.views.detail_v2', name='productDetail'),

    
    # url(r'^sample/$', 'sample.views.sample_home',name='sample_home'),
    # url(r'^samplesave/$', 'sample.views.sample_save',name='sample_save'),
    # # url(r'^advertisement/(?P<categoryname>.*)/(?P<id>\d+)$', 'adjod.views.sub_category1',name='sub_category1'),
    # url(r'^advertisement/(?P<subcategoryname>.*)/(?P<subid>\d+)$', 'adjod.views.view_ads',name='view_ads'),
    # url(r'^elasticsearch/$', 'advertisement.views.notes',name='notes'),
    # url(r'^search/', include('haystack.urls')),
    # url(r'^confirm/(?P<confirmation_code>.*)/(?P<username>.*)/', 'adjod.views.confirm',name='confirm' ),
    

    # url(r'^search/category/$', 'advertisement.views.search',name='search_by_categoryid'),

    

  
    # url(r'^(?i)debugsearch/', FacetedSearchView(
    #   template='fixido/debugsearch.html', 
    #   form_class=ProductSearchFilter, 
    #   # results_per_page=settings.SEARCH_PAGE_NUMBER_OF_LEADS
    # )),

    
    url(r'^(?i)apidocs/', include('fxapi.urls')),
    url(r'^searchnew/$', 'advertisement.views.searchnew',name='searchnew'),
    url(r'^(?P<name>.*)$', 'advertisement.views.sub_category',name='sub_category'),
    
)

# register_seo_admin(admin.site, MyMetadata)

   