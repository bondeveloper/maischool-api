from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from account.serializers import AccountSerializer


class RetrieveAccountView(generics.RetrieveAPIView):
    serializer_class = AccountSerializer
    permission_class = (IsAuthenticated,)