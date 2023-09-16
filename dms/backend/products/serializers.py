from .models import product
from rest_framework import serializers

class productSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    def get_my_discount(self, obj):
        return obj.get_discount()