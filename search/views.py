# from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

# Create your views here.
class SearchProductView(ListView):
    # queryset = Product.objects.all()
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
      context = super(SearchProductView, self).get_context_data(*args, **kwargs)
      query = self.request.GET.get('q')
      context['query'] = query
      # SearchQuery.objects.create(query=query)
      return context

    # def get_context_data(self, *args, **kwargs):
    #   context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #   print(context)
    #   return context

    def get_queryset(self, *args, **kwargs):
      
        request = self.request
        # print(request.GET)
        # query = request.GET.get('q')
        method_dict = request.GET
        # query = method_dict.get('q', "shirt")
        query = method_dict.get('q', None)
        # print(method_dict)
        # print(query)
    
        if query is not None:
          # lookups = Q(title__icontains=query) | Q(description__icontains=query)
          # return Product.objects.filter(lookups).distinct()
          return Product.objects.search(query)
        '''
        __icontains = field contains this
        __iexact = field is exactly this

        '''
        return Product.objects.featured()