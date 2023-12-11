from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product, Review, Order, OrderItem, ShippingAddress
from .serializers import ProductSerializer, ReviewSerializer, UserSerializer, UserSerializerWithToken, OrderSerializer
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/products/',
        'api/products/create/',
        'api/products/upload/',
        'api/products/<id>/reviews/',
        'api/products/top/',
        'api/products/<id>/',
    ]
    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    query = request.GET.get('keyword')
    if query == None:
        query = ''
    
    products = Product.objects.filter(name__icontains = query).order_by('-_id')

    page = request.GET.get('page')
    paginator = Paginator(products, 10)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage :
        products = paginator.page(paginator.num_pages)

    if page == None:
        page = 1
    page = int(page)

    serializer = ProductSerializer(products, many=True)
    return Response({'products': serializer.data, 'page': page, 'pages': paginator.num_pages})

@api_view(['GET'])
def getTopProducts(request):
    products = Product.objects.filter(rating__gte=4).order_by('-rating')[0:5]
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

