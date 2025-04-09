from rest_framework.generics import GenericAPIView
from .serializers import  ProfileSerializer 
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions




class ProfileAPIView(GenericAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self , request , *args , **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    def post(self, request , *args , **kwargs):
        user = request.user
        serializer = self.get_serializer(instance=user , data=request.data , partial=True)


        if serializer.is_valid():
            response = serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(data=serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self , request , *args , **kwargs):
        request.user.delete()
        return Response({"message":"User profile deleted successfully"})
    

__all__=["ProfileAPIView"]

