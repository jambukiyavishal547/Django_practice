from django.shortcuts import render
from .serializers import BlogSerializer,AuthorSerializer
from rest_framework.response import Response
from rest_framework import generics,mixins
from .models import Author,Blog
# Create your views here.
class BlogList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class AuthorList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class BlogDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AuthorDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    #----------------------------------------------------------------------------------------------------
# class BlogList(APIView):
#     def get(self, format=None):
#         blogs= Blog.objects.all()
#         serializer = BlogSerializer(blogs, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class BlogDetail(APIView):

#     def get_object(self,pk):
#         try:
#             return Blog.objects.get(pk=pk)
#         except Blog.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk, format=None):
#         blog = self.get_object(pk)
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)
    
#     def put(self, request, pk, formate=None):
#         blog = self.get_object(pk)
#         serializer = BlogSerializer(blog, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=False):
#         blog = self.get_object(pk)
#         blog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)