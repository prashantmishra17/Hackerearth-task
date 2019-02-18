from rest_framework import viewsets
from rest_framework import generics
from .models import WineCollection
from .serializers import WineCollectionSerializer



class Wines(generics.ListAPIView):
    queryset = WineCollection.objects.all()
    serializer_class = WineCollectionSerializer
    # context_dict={'wine_collection':wine_collection}
    # return render(request, 'index.html', context_dict)
