from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer, RegisterSerializer
from .models import Product
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .forms import Register, RegistrationForm
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User

# Create your views here.


@api_view(['GET'])
def index(request):
    return Response("Hello")


@api_view(["GET"])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getProduct(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# NEW
@api_view(["POST"])
def register(request):
    if request.method == 'POST':
        print("REQ DATA: ", request.data)

        form = RegistrationForm(data=request.data.get('user'))
        # print("SERIZLIZER DATA: ", serializer.data)
        if form.is_valid():
            # print("SERIZLIZER DATA: ", serializer.data)
            form.save()
            print("FORM DATA: ", form.data)
            return Response(form.data, status=status.HTTP_201_CREATED)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
