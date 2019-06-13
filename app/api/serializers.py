from rest_framework import serializers
from app.models import Currency, User, Account


class CurrencySerializer(serializers.ModelSerializer):

    def validate(self, data):
        if len(data['code']) != 3:
            raise serializers.ValidationError(f'Currency code <{data["code"]}> is too short/long. Expected 3')
        # TODO: add check for digits
        # TODO: uppercase
        return data

    class Meta:
        model = Currency
        fields = ('id', 'code',)


class AccountSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer(read_only=True)

    class Meta:
        model = Account
        fields = ('id', 'name', 'currency', 'balance')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
