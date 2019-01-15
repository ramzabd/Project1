from rest_framework.serializers import ModelSerializer
from apiApp.models import Contact
class ContactListAPIView(ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id',
            'name',
            'number',
            'email',
        ]
