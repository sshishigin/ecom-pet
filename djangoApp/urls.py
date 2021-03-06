from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from cart.views import CartAPI
from djangoApp.routers import DefaultRouterWithSimpleViews
from orders.views import OrderAPI, OrderItemViewSet
from shop.views import ItemsViewSet, LikeAPI
from users.views import UserViewSet, CustomTokenObtain

router = DefaultRouter()
router.register('api/items', ItemsViewSet)
router.register('api/users', UserViewSet)
router.register('api/orderItems', OrderItemViewSet)

extra_router = DefaultRouterWithSimpleViews()
extra_router.register('api/cart', CartAPI, 'cartAPI')
extra_router.register('api/order', OrderAPI, 'orderAPI')
extra_router.register('api/like', LikeAPI, 'likeAPI')

urlpatterns = [
    path('', admin.site.urls),
    path('api/login', CustomTokenObtain.as_view(), name='auth-token'),
]

urlpatterns += router.urls
urlpatterns += extra_router.urls
