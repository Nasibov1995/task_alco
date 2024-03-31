from rest_framework import serializers
from . models import CustomUser,BlockedIP
import io
import xlsxwriter

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
    def create(self, validated_data):
        validated_data['ip_address'] = self.context.get('request').META.get("REMOTE_ADDR")
        return CustomUser.objects.create(**validated_data)
        
        
class UserExcelSerializer(serializers.Serializer):
    def to_excel(self, queryset):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        headers = list(self.validated_data[0].keys())
        for col, header in enumerate(headers):
            worksheet.write(0, col, header)

        for row, user_data in enumerate(self.validated_data, start=1):
            for col, value in enumerate(user_data.values()):
                worksheet.write(row, col, value)

        workbook.close()
        return output.getvalue()
        
        
class BlockedIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockedIP
        fields = '__all__'