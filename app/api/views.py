from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions

from app.models import Currency, Account, User
from app.api.serializers import CurrencySerializer, AccountSerializer, \
    UserSerializer
from rest_framework import status


class CurrencyViewSet(viewsets.ModelViewSet):
    """
    Currency CRUD
    """
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            u_obj = User.objects.prefetch_related('currencies').get(id=user.id)
            return u_obj.currencies
        else:
            return None

    def create(self, request, *args, **kwargs):
        data = request.data.dict()
        serializer = CurrencySerializer(data=data)
        if serializer.is_valid():
            c = serializer.save()
            request.user.currencies.add(c.id)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountViewSet(viewsets.ModelViewSet):
    """
    Money Account CRUD
    """
    queryset = Account.objects.all().order_by('-id')
    serializer_class = AccountSerializer

    def create(self, request, *args, **kwargs):
        user_data = request.data.dict()
        user_data['balance'] = float(user_data['balance'])

        serializer = AccountSerializer(data=user_data)
        if serializer.is_valid():
            curr = Currency.objects.get(id=int(user_data['currency']))
            acc = serializer.save(currency=curr)
            request.user.accounts.add(acc.id)
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    """
    User CRUD
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        user_data = request.data.dict()
        user_data['password'] = make_password(user_data['password'])
        serializer = UserSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginApi(APIView):

    def post(self, request):
        user_data = request.data.dict()
        user = authenticate(username=user_data['username'],
                            password=user_data['password'])
        if user:
            login(request, user)
            return Response({}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Wrong user credentials'},
                            status=status.HTTP_400_BAD_REQUEST)
