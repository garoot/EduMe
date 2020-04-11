from .models import Blog, BlogSection, BlogComment
from rest_framework import serializers

class BlogSectionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogSection
        fields = '__all__'

class BlogCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = '__all__'

class BlogDetailSerializer(serializers.ModelSerializer):
    sections = BlogSectionDetailSerializer(many=True)
    comments = BlogCommentsSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class BlogForList(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['blog_title', 'blog_description',
                  'publish_date', 'blog_picture']
