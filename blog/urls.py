from django.urls import path
from .views import postDetail, home,register,loginPage,postDelete,postCreate,logoutPage,postUpdate

urlpatterns = [
    path('', home,name = 'home'),
    path('post_detail/<int:pk>/<slug:slug>',postDetail.as_view(),name='post_detail'),
    path('register/', register,name = 'register'),
    path('login/', loginPage,name = 'login'),
    path('logout/', logoutPage,name = 'logout'),
    path('post-create/', postCreate,name = 'post-create'),
    path('post-update/<int:pk>', postUpdate,name = 'post-update'),
    path('post-delete/<int:pk>', postDelete,name = 'post-delete'),
]