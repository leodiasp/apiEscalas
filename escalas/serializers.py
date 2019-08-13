from rest_framework import serializers
from .models import Escalas

class EscalasSerializer(serializers.ModelSerializer):

    class Meta:

        model = Escalas
        fields = '__all__'
