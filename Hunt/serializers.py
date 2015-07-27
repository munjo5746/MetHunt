from rest_framework import serializers
from Hunt.models import Hunt
from Hunt.models import Item

class HuntBeginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hunt
        fields = ('Title', 'Start', 'Category', 'Items')
