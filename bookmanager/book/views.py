from django.db.models import Q, F
from django.shortcuts import render


# Create your views here.
from book.models import BookInfo


def index(request):
    # BookInfo(name='三体3死神永生').save()
    print(BookInfo.objects.all())
    print(BookInfo.objects.get(id=1))
    print(BookInfo.objects.filter(name__icontains='三'))
    print(BookInfo.objects.filter(name__icontains='三').filter(id__gt=2))
    print(BookInfo.objects.exclude(name__icontains='三').exclude(id__gt=2))
    print(BookInfo.objects.filter(Q(name__icontains='三') & Q(id__gt=2)))
    # print(BookInfo.objects.filter(F(name__icontains='三'), F(id=2)))
    return render(request, 'index.html')
