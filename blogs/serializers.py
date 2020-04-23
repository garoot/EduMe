from .models import Blog, BlogComment
from rest_framework import serializers
from django.utils.html import strip_tags


#USED IT BEFORE TO INCLUDE IT IN ONE ADMIN CONTROL PAGE (Blogs)
    # class BlogSectionDetailSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = BlogSection
    #         fields = '__all__'

class BlogCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = '__all__'

class BlogDetailSerializer(serializers.ModelSerializer):
    #USED IT BEFORE TO INCLUDE IT IN ONE ADMIN CONTROL PAGE (Blogs)
        #sections = BlogSectionDetailSerializer(many=True)
    full_name = serializers.CharField(source='author.full_name')
    comments = BlogCommentsSerializer(many=True, read_only=True)
    # publish_date = serializers.DateField(format="%Y-%m-%d %H:%M:%S")
    
    class Meta:
        model = Blog
        read_only_fields = ['blog_category']
        fields = '__all__'

    # removes the tags CKEditor returns with the content
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['content'] = strip_tags(instance.content)
    #     return data
        # fields = ('blog_title', 'blog_description',
        #           'publish_date', 'blog_picture', 'content', 'author', 'comments')

class BlogSerializer(serializers.ModelSerializer):
    #USED IT BEFORE TO INCLUDE IT IN ONE ADMIN CONTROL PAGE (Blogs)
        # sections = BlogSectionDetailSerializer(many=True)
    # comments = BlogCommentsSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        read_only_fields = ['blog_category']
        fields = '__all__'
        # fields = ('blog_title', 'blog_description',
        #           'publish_date', 'blog_picture', 'content')

class BlogForList(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['blog_title', 'blog_description',
                  'publish_date', 'blog_picture']
