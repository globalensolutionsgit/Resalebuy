# coding: utf-8 
# -*- coding: utf-8 -*-
from django.shortcuts import redirect
# from haystack.views import SearchView
from search.searchsites import SearchView
# from fixido.util import get_global_language
from advertisement.models import *

class AdjodSearchView(SearchView):        
    def __call__(self, request):        
        print "advalue-1", request.REQUEST['q']
        if 'q' in request.REQUEST and unicode(request.REQUEST['q']).isdigit(): 
            print "advalue-11"           
            productid = long(request.REQUEST['q'])            
            if Product.objects.filter(id__exact=productid).exists():
                print "advalue-12"           
                return redirect('productDetail', productid)

        query_string = request.META.get('QUERY_STRING', '').split('&')
        qsl = [qs for qs in query_string if qs.startswith('q=')]
        query = qsl[0].replace('q=', '').decode('latin1') if qsl else u''
        print "advalue-14", query           
        if u'�' in request.REQUEST.get('q', u''):
            print "advalue-15"           
            if request.method == "GET":
                print "advalue-16"           
                request.GET._mutable = True
                request.GET['q'] = query
                request.GET._mutable = False
                print "advalue-17"               
            elif request.method == "POST":
                print "advalue-18"           
                request.POST._mutable = True
                request.POST['q'] = query
                request.POST._mutable = False
                print "advalue-19"           
        print "advalue-20"                   
        return super(AdjodSearchView, self).__call__(request)