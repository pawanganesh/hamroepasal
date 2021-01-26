from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     DestroyAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     )

from .models import Category, SubCategory, Brand, Product
from .serializers import (CategoryModelSerializer,
                          SubCategoryModelSerializer,
                          ProductModelSerializer,
                          BrandModelSerializer)


# 127.0.0.1:8000/api/product/category/list/
class CategoryModelListAPIView(ListAPIView):
    serializer_class = CategoryModelSerializer

    def get_queryset(self):
        return Category.objects.all()

# 127.0.0.1:8000/api/product/sub-category/list/
class SubCategoryModelListAPIView(ListAPIView):
    serializer_class = SubCategoryModelSerializer

    def get_queryset(self):
        return SubCategory.objects.all()


class ProductModelListAPIView(ListAPIView):
    serializer_class = ProductModelSerializer

    def get_queryset(self):
        return Product.objects.all()


class BrandModelListAPIView(ListAPIView):
    serializer_class = BrandModelSerializer

    def get_queryset(self):
        return Brand.objects.all()


class CategoryModelCreateAPIView(CreateAPIView):
    serializer_class = CategoryModelSerializer


class SubCategoryModelCreateAPIView(CreateAPIView):
    serializer_class = SubCategoryModelSerializer


class BrandModelCreateAPIView(CreateAPIView):
    serializer_class = BrandModelSerializer


class ProductModelCreateAPIView(CreateAPIView):
    serializer_class = ProductModelSerializer


class CategoryModelDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()


class SubCategoryModelDestroyAPIView(DestroyAPIView):
    queryset = SubCategory.objects.all()


class BrandModelDestroyAPIView(DestroyAPIView):
    queryset = Brand.objects.all()


class ProductModelDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()


class CategoryModelRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class SubCategoryModelRetrieveAPIView(RetrieveAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryModelSerializer


class BrandModelRetrieveAPIView(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandModelSerializer


class ProductModelRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class CategoryModelUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class SubCategoryModelUpdateAPIView(UpdateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryModelSerializer


class BrandModelUpdateAPIView(UpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandModelSerializer


class ProductModelUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
