from django import template
from django.db.models import *
from advertisement.models import *
from banner.models import *
from adjod.views import *
# from django.contrib.gis.geoip import GeoIP
register = template.Library()

@register.filter
def get_photos(photo): 
    photo=str(photo).split(',')
    return photo[0]

@register.filter
def get_videos(video):    
    video=str(video).split(',')
    return video[0]

@register.filter
def get_categories(initial_load):  
	category=Category.objects.all()	
	return category

@register.filter
def get_subcategories(categoryId):  	
	subcategories = SubCategory.objects.filter(category_id=categoryId)		
	return subcategories	

@register.filter
def get_subcategoriesCount(subCategoryId):  
	subcategoriescounts = Product.objects.filter(subcategory_id=subCategoryId, status_isactive=1).count()          		
	# subcategoriescounts = Product.objects.filter(subcategory_id=subCategoryId).annotate(Count('subcategory'))			
	return subcategoriescounts

@register.filter
def get_brandforsubcategory(subCategoryId):  	
	brandforsubcategory = Dropdown.objects.filter(subcat__id=subCategoryId).exclude(brand_name='')
	return brandforsubcategory	

@register.filter
def get_banner(banner):
	banner=SiteBanner.objects.all()
	return banner

@register.filter
def conversion(price):
    # return 1
	return convert(price)



