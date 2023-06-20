from rest_framework import serializers
from planApp.models import Plan


class PlanSerializer(serializers.ModelSerializer):
    #이부분 이해안감 물어보기
    user = serializers.StringRelatedField(read_only=True)
    plan_id = serializers.IntegerField(source='id', read_only=True)
    class Meta:
        model = Plan
        fields = {
            'plan_id',
            'user',
            'date',
            'content',
            'is_checked',
            'emoji',
        }