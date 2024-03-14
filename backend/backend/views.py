from rest_framework import generics, response, status, permissions


class HomeAPIView(generics.GenericAPIView):
    """
    An endpoint for Home 
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return response.Response(request.data, status=status.HTTP_200_OK)
