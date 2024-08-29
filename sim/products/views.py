from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .models import *
from django.core.serializers import serialize
import json



def add_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            seller_id = data['seller_id']
            seller = Seller.objects.get(id=seller_id)
            if seller.is_Confirmed:
                name_product = data['name']
                description = data['description']
                price = data['price']
                
                new_product = Product.objects.create(
                    name=name_product,
                    description=description,
                    price=price,
                    seller=seller
                )
                
                return JsonResponse({'message': 'Product added successfully'})
            else:
                return JsonResponse({'error': 'Seller not confirmed'})
        except Seller.DoesNotExist:
            return JsonResponse({'error': 'Seller does not exist'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'})


def product_list(request):
    products = Product.objects.all()
    result = []
    for item in products:
        product_dict = {
            "name": item.name,
            "description": item.description,
            "price": item.price,
            "seller": item.seller.id, 
        }
        result.append(product_dict)
    
    return JsonResponse(result, safe=False)


