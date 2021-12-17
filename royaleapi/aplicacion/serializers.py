from rest_framework import serializers

class APISerializer(serializers.Serializer):
    id = serializers.IntegerField()
    alias = serializers.CharField(max_length=45)
    tag = serializers.CharField(max_length=12)
    idioma = serializers.CharField(max_length=9)
    usoTotal = serializers.IntegerField()