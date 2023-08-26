from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from ramuriAPI.serializers import UserSerializer, GroupSerializer, BrandSerializer
from ramuriAPI.models import Brand
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.decorators import api_view

class ListBrands(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    # def get(self, request, format=None):
    #     brands = Brand.objects.all()
    #     serializer = BrandSerializer(brands, many=True)
    #     return Response(serializer.data)
    
    # def post(self, request, format=None):
    #     serializer = BrandSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BrandDetail(APIView):

    def get(self, request, url):
        brand = Brand.objects.filter(urls__contains=[url])
        serializer = BrandSerializer(brand, many=True)
        return Response(serializer.data)
    
    def put(self, request, url, format=None):
        brand = Brand.objects.filter(url=url)
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BrandViewSet(viewsets.ModelViewSet):
    """
    API endpoint that shows brands.
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


# class BrandReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     A viewset that provides the standard actions
#     """
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer
#     lookup_field = 'url'

    # @action(detail=True)
    # def group_names(self, request, pk=None):
    #     """
    #     Returns a list of all the group names that the given
    #     user belongs to.
    #     """
    #     user = self.get_object()
    #     groups = user.groups.all()
    #     return Response([group.name for group in groups])

@api_view()
def brand_list(request):
    try:
        queryset = Brand.objects.all()
        data = core_serializers.serialize('json', queryset)
        return HttpResponse(data)
        
        return Response(brand)
    except Brand.DoesNotExist:
        raise Http404("Brand does not exist")

# @api_view()
# def brand_detail(request, url):
#     try:
#         queryset = Brand.objects.filter(url=url)
#         data = core_serializers.serialize('json', queryset)
#         return HttpResponse(data)
        
#         return Response(brand)
#     except Brand.DoesNotExist:
#         raise Http404("Brand does not exist")



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer



class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
