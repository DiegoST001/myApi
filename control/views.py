from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Categoria, Producto
from .serializar import CategoriaSerializer, ProductoSerializer


class IndexView(APIView):
    
    def get(self, request):
        context = {'mensaje': 'servidor activo'}
        return Response(context)

class CategoriaView(APIView):

    def get_queryset(self):
        return Categoria.objects.all() 

    def get(self, request):
        categorias = self.get_queryset() 
        serCategorias = CategoriaSerializer(categorias, many=True)
        return Response(serCategorias.data)

    def post(self, request):
        serCategoria = CategoriaSerializer(data=request.data)
        serCategoria.is_valid(raise_exception=True)
        serCategoria.save()
        return Response(serCategoria.data, status=status.HTTP_201_CREATED)


class CategoriaDetailView(APIView):

    def get_queryset(self):
        return Categoria.objects.all()  

    def get(self, request, categoria_id):
        categoria = self.get_queryset().get(pk=categoria_id)
        serCategoria = CategoriaSerializer(categoria)
        return Response(serCategoria.data)

    def put(self, request, categoria_id):
        categoria = self.get_queryset().get(pk=categoria_id)
        serCategoria = CategoriaSerializer(categoria, data=request.data)
        serCategoria.is_valid(raise_exception=True)
        serCategoria.save()
        return Response(serCategoria.data)

    def delete(self, request, categoria_id):
        categoria = self.get_queryset().get(pk=categoria_id)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductoView(APIView):

    def get_queryset(self):
        return Producto.objects.all()  

    def get(self, request):
        productos = self.get_queryset() 
        serProductos = ProductoSerializer(productos, many=True)
        return Response(serProductos.data)

    def post(self, request):
        serProducto = ProductoSerializer(data=request.data)
        serProducto.is_valid(raise_exception=True)
        serProducto.save()
        return Response(serProducto.data, status=status.HTTP_201_CREATED)


class ProductoDetailView(APIView):

    def get_queryset(self):
        return Producto.objects.all()  
    
    def get(self, request, producto_id):
        producto = self.get_queryset().get(pk=producto_id)
        serProducto = ProductoSerializer(producto)
        return Response(serProducto.data)

    def put(self, request, producto_id):
        producto = self.get_queryset().get(pk=producto_id)
        serProducto = ProductoSerializer(producto, data=request.data)
        serProducto.is_valid(raise_exception=True)
        serProducto.save()
        return Response(serProducto.data)

    def delete(self, request, producto_id):
        producto = self.get_queryset().get(pk=producto_id)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
