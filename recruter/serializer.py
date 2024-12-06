from rest_framework import serializers
from .models import JobPosting

class JobPostingSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True) 
    job_title = serializers.CharField(max_length=100)
    description = serializers.CharField()

    class Meta:
        model = JobPosting
        fields = ['user', 'job_title', 'description', 'job_type', 'salary', 'place']

    def create(self, validated_data):
        user = self.context['request'].user
        job_posting = JobPosting.objects.create(user=user, **validated_data)
        return job_posting
