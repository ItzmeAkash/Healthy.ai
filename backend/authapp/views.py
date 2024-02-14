import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer

class UserRegisterView(APIView):
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                user.is_active = True
                user.save()

                return Response({'messages': 'Reguisteration Success'})

        except Exception as e:
            error_messages = str(e)
            required_messages = {}
            # Error message filtering
            for match in re.finditer(r"'(.*?)': \[ErrorDetail\(string='(.*?)', code='(.*?)'\)\]", error_messages):
                field, message = match.group(1), match.group(2)
                if field != 'unknown':  
                    required_messages[field] = message

            return Response({'messages': required_messages}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
