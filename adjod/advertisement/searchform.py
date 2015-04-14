import re
from django import forms
from collections import OrderedDict
import advertisement
from haystack.forms import SearchForm, FacetedSearchForm
from datetime import datetime
from django.http import HttpResponse, Http404
from advertisement.search import search as productsearch

from haystack.query import SearchQuerySet
from haystack.inputs import Clean, Raw
from haystack.query import SQ

from models import Product

class Partial(Clean):
    input_type_name = 'partial'
    post_process = True

    def __init__(self, query_string, **kwargs):
        self.original = query_string
        super(Partial, self).__init__(query_string, **kwargs)

    def prepare(self, query_obj):
        query_string = super(Partial, self).prepare(query_obj)
        query_string = query_string.lower()
        query_string = re.sub( '\s+', '* ', query_string).strip()

        if query_string[-1] != '*':
          query_string = query_string + u'*'

        print "Searching", self.original, query_string
        return 

class ProductSearchFilter(FacetedSearchForm):

#Code included by Ramu
    model = None

    # def __init__ (self,request=None, using=None):
    #     from models import Lead
    #     self.model= Lead#kwargs.pop('models')        
    #     super(LeadSearchFilter,self).__init__(request, using=using, **kwargs)

    
   

    locality = forms.CharField(required=False)
    category = forms.CharField(required=False)

    

    def no_query_found(self):
        
      data = self.searchqueryset.all()  
        
      if hasattr(self, 'cleaned_data'):
          save_object = None

          # if self.cleaned_data['sortdata']:
          #     if (self.cleaned_data['sortdata'] == "created_date"):
          #       data = data.all().order_by('-created_date')
              
          #     if (self.cleaned_data['sortdata'] == "modified_date"):
          #      data = data.all().order_by('-modified_date')
              
              
      return data

    def get_default_queryset(self):
      sqs = SearchQuerySet().all()
      sqs = sqs.models(Product)
      return sqs.all().order_by('-created_date')

    def get_default_filters(self):
      return None

    def get_default_search_field(self):
      return 'searchtext'

    def get_model_class(self):
      return Product


    def searchv2(self):
      if not hasattr(self, 'cleaned_data'):

        return productsearch(model_cls=self.get_model_class()) 
          # default_filters=self.get_default_filters())
        
      _params = [
        'locality',
        'category',
        
      ]

      params = OrderedDict()
      for p in _params:
        if p in self.cleaned_data and self.cleaned_data[p]:
          params[p] =  self.cleaned_data[p]
        else:
          params[p] =  None

      
      
      if params['locality']:
        params['locality'] = params['locality'].split(',')

      q = self.cleaned_data['q'] if 'q' in self.cleaned_data else None
      groupby = None
      orderby = None

      orderby_mappings = {
        'createddate': '-created_date',
        'modifieddate': '-modified_date',
        # 'pricelow': 'base_price',
        # 'pricehigh': '-base_price'
      }

      

      # if not orderby:
      #   orderby = orderby_mappings['createddate']        
      print "not in if searchv2"
      return productsearch(q, params, orderby, model_cls=self.get_model_class(), 
        default_filters=self.get_default_filters(), 
        default_search_field=self.get_default_search_field())

    def search(self):
        print "search"
        # return self.searchv2()
        print "search1"
        sqs = self.get_default_queryset()
        print "search sqs", sqs
        search_field = self.get_default_search_field()
        print search_field
        if hasattr(self, 'cleaned_data'):
          original_query = self.cleaned_data['q']

          # Split by special character and space
          query = re.sub(r'[^\w]', ' ', original_query, 
            flags=re.UNICODE).split(' ')
          print "query", query

          # Remove empty and special characters
          query = [q for q in query \
            if q and (not re.match(r'[^\w]', q, flags=re.UNICODE))]
          print "query", query
          # if query:
          #   # For some reason, if the query has '/' character, haystack gives
          #   # empty result and throws exception in elastic. "Clean" does not
          #   # clean this character. So remove this character manually with
          #   # space  
          #   original_query = original_query.replace('/', ' ')

          #   cleand = Clean(original_query)
          #   qs = SQ(**{search_field:cleand})
          #   qs = qs | SQ(**{search_field + '__startswith': cleand})

          #   cleand_q = ' '.join(query)
          #   if original_query != cleand_q:
          #     qs = qs | SQ(**{search_field:cleand_q})

          #   # if len(query) > 1:
          #   #   for q in query:
          #   #     qs = qs | SQ(**{search_field + '__startswith':Clean(q)})

          #   sqs = sqs.filter(qs)

        if hasattr(self, 'cleaned_data'):

          save_object = None
          
          # if self.cleaned_data['save_search']:
          #   save_object = LeadFilter()
  
          # if self.cleaned_data['lang']:
          #     selLang = self.cleaned_data['lang']
          #     if selLang =='en':
          #         sqs = sqs.filter(language__in=['en','sv'])
          #     else:
          #         sqs = sqs.filter(language=self.cleaned_data['lang'])
                  
                
          # if self.cleaned_data['budget_start']:
          #     sqs = sqs.filter(budget__gte=self.cleaned_data['budget_start'])
          #     if save_object:
          #       save_object.budget_from = self.cleaned_data['budget_start']
  
          # if self.cleaned_data['budget_end']:
          #     sqs = sqs.filter(budget__lte=self.cleaned_data['budget_end'])
          #     if save_object:
          #       save_object.budget_to = self.cleaned_data['budget_end']
  
          # if self.cleaned_data['deal_start']:
          #     sqs = sqs.filter(deal_starts__gte=self.cleaned_data['deal_start'])
          #     if save_object:
          #       save_object.deal_time_from = self.cleaned_data['deal_start']
  
          # if self.cleaned_data['deal_end']:
          #     sqs = sqs.filter(deal_ends__lte=self.cleaned_data['deal_end'])
          #     if save_object:
          #       save_object.deal_time_to = self.cleaned_data['deal_end']  
  
          # if self.cleaned_data['price_start']:
          #     sqs = sqs.filter(price__gte=self.cleaned_data['price_start'])
          #     if save_object:
          #       save_object.price_from = self.cleaned_data['price_start']  
                  
          # if self.cleaned_data['price_end']:
          #     sqs = sqs.filter(price__lte=self.cleaned_data['price_end'])
          #     if save_object:
          #       save_object.price_to = self.cleaned_data['price_end']  
  
          if self.cleaned_data['locality']:
              sqs = sqs.filter(locations__in=self.cleaned_data['locality'].split(','))
              if save_object:
                save_object.location = self.cleaned_data['locality']  
                
                    
          
   
          # if self.cleaned_data['sortdata']:
          #     if (self.cleaned_data['sortdata'] == "createddate"):
          #       sqs = sqs.all().order_by('-created_date')
              
          #     if (self.cleaned_data['sortdata'] == "modifieddate"):
          #      sqs = sqs.all().order_by('-modified_date')
              
          
          # if self.cleaned_data['groupby']:
          #   groupby = self.cleaned_data['groupby']
          #   sqs = sqs.facet(groupby)
        # print "sqs value", sqs
        return sqs#sqs.models(self.model)


