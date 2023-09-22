# Import necessary modules
from .models import product  # Import the Product model
from rest_framework import serializers  # Import serializers module from Django Rest Framework

# Create a serializer class for the Product model
class ProductSerializer(serializers.ModelSerializer):
    # Define a custom field 'my_discount' that will be calculated using the 'get_my_discount' method
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = product  # Specify the model to be serialized (Product in this case)
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]  # Specify which fields from the model to include in the serialized representation

    # Define a method to calculate the 'my_discount' field
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, product):
            return None
        return obj.get_discount()
