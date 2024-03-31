from rest_framework import permissions, status
from rest_framework.response import Response
import xlsxwriter
from django.http import HttpResponse
from main.models import CustomUser,BlockedIP
from main.serializers import CustomUserSerializer,BlockedIPSerializer
from rest_framework import generics
import io
from rest_framework.generics import GenericAPIView,CreateAPIView
from rest_framework.permissions import IsAdminUser


class UserExtractionAPIView(generics.GenericAPIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        # Get the list of user IDs from query parameters
        user_ids = request.GET.getlist('user_ids', [])
        
        queryset = CustomUser.objects.filter(id__in=user_ids)
        
        # If no specific user IDs are provided, return all users
        if not user_ids:
            queryset = CustomUser.objects.all()

        serializer = CustomUserSerializer(queryset, many=True)

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        headers = list(serializer.data[0].keys())
        for col, header in enumerate(headers):
            worksheet.write(0, col, header)

        for row, user_data in enumerate(serializer.data, start=1):
            for col, value in enumerate(user_data.values()):
                if isinstance(value, list):
                    value = ', '.join(value)  # Convert list to string
                worksheet.write(row, col, value)    

        workbook.close()
        
        # Create response with Excel file
        response = HttpResponse(output.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="user_data.xlsx"'
        return response


class BlockIPApi(GenericAPIView):
    serializer_class = BlockedIPSerializer
    permission_classes = [IsAdminUser]

    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            ip_adresses = BlockedIP.objects.all()
            ip_address = 0
            for ip in ip_adresses:
                ip_address = ip.blocked_ip_address
                
            # Check if the IP address is associated with any active user
            user_with_ip = CustomUser.objects.filter(ip_address=ip_address, is_active=True)
            for user_with_ip in user_with_ip:
                user_with_ip.is_active = False
                user_with_ip.save()
        
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:    
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


