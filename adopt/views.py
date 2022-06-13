from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from adopt.serializers import AdoptSerializer
from .email_service import send_confirmation_email
from .models import Adopt


class AdoptList(APIView):
    def get(self, request, format=None):
        adoptions = Adopt.objects.all()
        serializer = AdoptSerializer(adoptions, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, format=None):
        serializer = AdoptSerializer(data=request.data)
        if serializer.is_valid():
            adopt = serializer.save()
            send_confirmation_email(adopt)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(
            {
                "errors": serializer.errors,
                "message": "Houveram erros de validação"
            },
            status=HTTP_400_BAD_REQUEST
        )
