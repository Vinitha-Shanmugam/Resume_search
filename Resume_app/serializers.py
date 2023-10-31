from rest_framework import serializers


class ResumeSearchSerializer(serializers.Serializer):
    search_query = serializers.CharField()
    user_name = serializers.CharField()
