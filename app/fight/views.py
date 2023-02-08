from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Serializer
from fight.serializers import FightSerializer
# Services
from fight.services import Fight


class FightAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Validating the data that is being sent to the API
        serializer = FightSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Validating the data that is being sent to the API.
        data = serializer.validated_data

        try:
            fight = Fight(data)
            fight.start()

            return Response(fight.story)
        except Exception as error:
            print(error)

        return Response(None, status=status.HTTP_400_BAD_REQUEST)
