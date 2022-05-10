from rest_framework import serializers
from users.models import BlockUser, ReportUser


class BlockUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockUser
        fields = "__all__"


class ReportUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportUser
        fields = "__all__"
