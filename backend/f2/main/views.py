import time
import json
from datetime import date
from decimal import *
from django.core import serializers
from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import connection
from django.db.models import Sum, Q
from django.db.models.functions import Coalesce
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from djmoney.money import Money
from main.models import Account, Category, Record
from main.serializers import UserSerializer, AccountSerializer, CategorySerializer, CategorySumOnRangeSerializer, RecordSerializer, AccountsBalanceSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    pagination_class = None
    #permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = None

    #permission_classes = [permissions.IsAuthenticated]

    @action(detail=True,
            methods=['GET'],
            url_path='sum/(?P<start_range>\d{4}-\d{2}-\d{2})-(?P<end_range>\d{4}-\d{2}-\d{2})')
    def summ(self, request, start_range, end_range, pk=None):
        if pk == '4':
            time.sleep(1)
        category = Category.objects.get(id=pk)
        children = Category.objects.filter(parent=category)
        records = Record.objects.filter(date__gte=start_range, date__lte=end_range, category=category).aggregate(Sum('value'))
        return Response(records)

    @action(detail=False,
            methods=['GET'],
            url_path='expenses')
    def expenses_only(self, request):
        categories = Category.objects.all().exclude(title='Income'
            ).exclude(parent__title='Income'
            ).exclude(title='_Service'
            ).exclude(parent__title='_Service')
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data)



class RecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows records to be viewed.
    """
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    #permission_classes = [permissions.IsAuthenticated]


    def create(self, request):
        print(request.data)
        serializer = RecordSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False,
            methods=['GET'],
            url_path='recent')
    def recent(self, request):
        records = Record.objects.all().order_by('date')[:10]
        serializer = self.get_serializer(records, many=True)
        return Response(serializer.data)


class RecordAutoSuggestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows records to be viewed.
    Pagination is turned off.
    """
    queryset = Record.objects.all().order_by('item').distinct('item')
    serializer_class = RecordSerializer
    pagination_class = None
    #permission_classes = [permissions.IsAuthenticated]


class AccountsBalanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that returns all accounts with accounts
    balance annotated
    """
    queryset = Account.objects.all().annotate(account_balance=Coalesce(Sum('record__value'), Decimal(0)))
    serializer_class = AccountsBalanceSerializer
    pagination_class = None


