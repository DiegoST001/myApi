from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('categorias/', views.CategoriaView.as_view(), name='categorias'),
    path('categorias/<int:categoria_id>/', views.CategoriaDetailView.as_view(), name='categoria-detail'),
    path('productos/', views.ProductoView.as_view(), name='productos'),
    path('productos/<int:producto_id>/', views.ProductoDetailView.as_view(), name='producto-detail'),
]
