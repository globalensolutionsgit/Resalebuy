from django.contrib.auth.models import *
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from adjod.models import *
from paypal.standard.ipn.models import PayPalIPN
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import payment_was_successful
import datetime
from haystack.query import SearchQuerySet
from django.views.decorators.csrf import csrf_exempt

TYPE = (
    ('buy', 'Buy'),
    ('sell', 'Sell'),
   
)

CONDITION = (
    ('used', 'Used'),
    ('new', 'New'),
   
)

YOU=( ('individual','Individual'),('dealer','Dealer'))
@csrf_exempt
def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    # You need to check 'payment_status' of the IPN

    if ipn_obj.payment_status == "Completed":
        # Undertake some action depending upon `ipn_obj`.
        if ipn_obj.custom == "Upgrade all users!":
            Users.objects.update(paid=True)
    

payment_was_successful.connect(show_me_the_money)

    
class Category(models.Model):
    icon = models.ImageField(upload_to='static/img/', blank=True)
    
    name = models.CharField(max_length=250)
    category_type = models.CharField(max_length=250)
    
    def __unicode__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category) 
    name = models.CharField(max_length=50) 
    
    
    def __unicode__(self):
        return self.name

class Dropdown(models.Model):
    
    subcat=models.ManyToManyField(SubCategory, null=True, blank=True)
    brand_name=models.CharField(max_length=50, blank =True,default='')
    # brand_refid=models.ForeignKey('self', blank=True, null=True)
    # model_name=models.CharField(max_length=50, blank =True, default='')
    # type_name=models.CharField(max_length=50, blank =True, default='')
    # year=models.CharField(max_length=50, blank =True,default='')
    # color=models.CharField(max_length=50, blank =True,default='')
    # os=models.CharField(max_length=50, blank =True,default='')
    # sim=models.CharField(max_length=50, blank =True,default='')
    # alsoinclude=models.CharField(max_length=50, blank =True,default='')

    def __unicode__(self):
        return self.brand_name

# class Brand(models.Model):
#     brand_name= models.CharField(max_length=50)
#     brand_subcategory=models.ManyToManyField(SubCategory)
#     model_name

#     def __unicode__(self):
#         return self.brand_name

class City(models.Model):
    city=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.city

class Locality(models.Model):
    city_refid=models.ForeignKey(City,null=True)
    locality=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.locality

class PremiumPriceInfo(models.Model):
    premium_price = models.FloatField(null=True, default=0.0)
    currency=models.CharField(max_length=10)
    purpose=models.CharField(max_length=30)
    month=models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.purpose

class Product(models.Model):
    userprofile=models.ForeignKey(UserProfile, null=True, blank=True)
    # user_id=models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='Chosen Category', null=False)
    subcategory =models.ForeignKey(SubCategory,null=False)
    adtype= models.CharField(max_length=10, choices=TYPE, null=False)
    title = models.CharField(max_length=250, null=False)
    photos = models.ImageField(upload_to='static/img/photos/',null=True, max_length=500)
    thumbnail = models.ImageField(upload_to="static/img/thumbs/", null=True, editable=False, max_length=500)
    imagecount=models.IntegerField(null=True, blank=True)
    video=models.FileField(upload_to='/static/videos/',null=True, blank=True)
    condition = models.CharField(max_length=10,choices=CONDITION)
    price = models.FloatField(null=True, default=0.0)
    ad_brand=models.ForeignKey(Dropdown,null=False, related_name="ad_brand")
    ad_year=models.CharField(max_length=10, null=True)
    city=models.ForeignKey(City, null=False)
    locality=models.ForeignKey(Locality, null=False)
    description = models.TextField(max_length=100, verbose_name="Description", null=False)
    you_are = models.CharField(max_length=20,choices=YOU,default='individual', null=False)
    you_name = models.CharField(max_length=20, null=True)
    you_email = models.CharField(max_length=30, null=False)
    you_phone = models.CharField(max_length=12, null=True)
    created_date =models.DateField(default=datetime.datetime.now)
    modified_date =models.DateField(default=datetime.datetime.now)
    isregistered_user=models.BooleanField(default=False)
    ispremium_ad=models.BooleanField(default=False)
    premium_plan=models.ForeignKey(PremiumPriceInfo, null=True, blank=True)
    expired_date=models.DateField(null=True,blank=True)
    status_isactive=models.BooleanField(default=False)
    
    class Admin:
        pass
  
    def __unicode__(self):
        return self.title

class FreeAlert(models.Model):
    alert_user=models.ForeignKey(UserProfile)
    alert_category = models.ForeignKey(Category, verbose_name='Chosen Category', null=False)
    alert_subcategory =models.ForeignKey(SubCategory,null=False)
    alert_brand=models.ForeignKey(Dropdown,null=False)
    alert_city=models.ForeignKey(City, null=False)
    alert_email=models.CharField(max_length=30, null=False)
    alert_mobile=models.CharField(max_length=30, null=False)
    mail_is_sent=models.BooleanField(default=False)
    last_email_sent = models.DateTimeField(null=True)
    def __unicode__(self):
        return self.alert_email

    def get_matching_filters(cls, product):
        ## STEP 1: Match by users search filter
        print "product.category", product.category
        print "product.subcategory", product.subcategory
        print "product.subcategory", product.subcategory
        qs = FreeAlert.objects.filter(product=product)
        print "qs", qs
        return qs



