from django.urls import path

from .views import (CategoryModelListAPIView,
                    SubCategoryModelListAPIView,
                    BrandModelListAPIView,
                    ProductModelListAPIView,

                    CategoryModelCreateAPIView,
                    SubCategoryModelCreateAPIView,
                    BrandModelCreateAPIView,
                    ProductModelCreateAPIView,

                    CategoryModelDestroyAPIView,
                    SubCategoryModelDestroyAPIView,
                    BrandModelDestroyAPIView,
                    ProductModelDestroyAPIView,

                    CategoryModelRetrieveAPIView,
                    SubCategoryModelRetrieveAPIView,
                    BrandModelRetrieveAPIView,
                    ProductModelRetrieveAPIView,

                    CategoryModelUpdateAPIView,
                    SubCategoryModelUpdateAPIView,
                    BrandModelUpdateAPIView,
                    ProductModelUpdateAPIView,

                    )


urlpatterns = [
    path('category/list/', CategoryModelListAPIView.as_view()),
    path('sub-category/list/', SubCategoryModelListAPIView.as_view()),
    path('brand/list/', BrandModelListAPIView.as_view()),
    path('product/list/', ProductModelListAPIView.as_view()),

    path('category/create/', CategoryModelCreateAPIView.as_view()),
    path('sub-category/create/', SubCategoryModelCreateAPIView.as_view()),
    path('brand/create/', BrandModelCreateAPIView.as_view()),
    path('product/create/', ProductModelCreateAPIView.as_view()),

    path('category/delete/<int:pk>/', CategoryModelDestroyAPIView.as_view()),
    path('sub-category/delete/<int:pk>/', SubCategoryModelDestroyAPIView.as_view()),
    path('brand/delete/<int:pk>/', BrandModelDestroyAPIView.as_view()),
    path('product/delete/<int:pk>/', ProductModelDestroyAPIView.as_view()),

    path('category/<int:pk>/', CategoryModelRetrieveAPIView.as_view()),
    path('sub-category/<int:pk>/', SubCategoryModelRetrieveAPIView.as_view()),
    path('brand/<int:pk>/', BrandModelRetrieveAPIView.as_view()),
    path('product/<int:pk>/', ProductModelRetrieveAPIView.as_view()),

    path('category/update/<int:pk>/', CategoryModelUpdateAPIView.as_view()),
    path('sub-category/update/<int:pk>/', SubCategoryModelUpdateAPIView.as_view()),
    path('brand/update/<int:pk>/', BrandModelUpdateAPIView.as_view()),
    path('product/update/<int:pk>/', ProductModelUpdateAPIView.as_view()),

]
