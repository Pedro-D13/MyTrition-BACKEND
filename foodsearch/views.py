from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from foodsearch.models import FoodCategory,FoodDescription


# Create your views here.

class ResultListView(ListView):
    model = FoodDescription
    context_object_name="results"
    template_name = 'foodsearch/results.html'

    def get_queryset(self):
        qs = super().get_queryset()
        food_results =  qs.filter(description__icontains=self.kwargs['query_string'])
        # food_cat = set(map(lambda x: FoodCategory.objects.get(id=x.food_category_id), food_results)) 

        return {'food':food_results}




    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['results'] = 
    #     return context


def iterate(result):
    foodcat =[]
    results = list(result)
    for each in results:
        if each.food_category_id != None:
            foodcat.append(FoodCategory.objects.get(id=each.food_category_id))
    return set(foodcat)

def result(request,query_string):
    results =  list(FoodDescription.objects.filter(description__contains=query_string))
    return render(request, 'foodsearch/results.html',{'results':results})


    
# return a set and then convert a list

'''
    for each in results:
        if each.food_category_id != None:
            category_options.append(FoodCategory.objects.get(id=each.food_category_id))
'''

# to get the Categorys the food they are looking up returns!
# category_ids = [FoodCategory.objects.get(id='x'.food_category_id) for 'x' in querystring if x.food_category_id != None]  
# category_set = set([x.description for x in cat_ids])
# category_set gives back the food category it fits into
# person will choose the set the are looking for get the id key of that e.i. Baked Products id = 18

# def FoodCategory(request,result):
#     category_options = [FoodCategory.objects.get(id=each.food_category_id) for each in result if each.food_category_id != None] 
#     category_set = set([x.description for x in category_options])




#apples.model.objects.filter(food_category_id=cat.id)
# for each in apples: 
    #  ...:     if each.food_category_id == 18: 
    #  ...:         ans.append(each) 