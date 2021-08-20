from django.contrib.auth.models import User
from rest_framework import serializers
from main.models import Account, Category, Record


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        fields = ['id', 'parent', 'title']


class CategorySumOnRangeSerializer(serializers.Serializer):
    value = serializers.FloatField()


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class AccountsBalanceSerializer(serializers.ModelSerializer):
    account_balance = serializers.DecimalField
    class Meta:
        model = Account
        fields = '__all__'
        extra_fields = ['account_balance']

    # override to allow adding extra field to
    # __all__ fields 
    # so I wouldn't have to explicitly write them
    def get_field_names(self, declared_fields, info):
        expanded_fields = super(AccountsBalanceSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields
