from .models import *
from rest_framework import serializers
from django.utils.html import strip_tags


#USED IT BEFORE TO INCLUDE IT IN ONE ADMIN CONTROL PAGE (Blogs)
    # class BlogSectionDetailSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = BlogSection
    #         fields = '__all__'


class BlogCommentsSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='user.full_name')
    comment_user = serializers.CharField(source='user.full_name')
    class Meta:
        model = BlogComment
        fields = '__all__'

class BlogDetailSerializer(serializers.ModelSerializer):
    #USED IT BEFORE TO INCLUDE IT IN ONE ADMIN CONTROL PAGE (Blogs)
        #sections = BlogSectionDetailSerializer(many=True)
    full_name = serializers.CharField(source='author.full_name')
    comments = BlogCommentsSerializer(many=True, read_only=True)
    likes = serializers.IntegerField(source='get_likes')
    dislikes = serializers.IntegerField(source='get_dislikes')

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

# can be called to CRUD likes passing user_id and blog_id
class BlogLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogLike
        fields = '__all__'


class BlogDislikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogDislike
        fields = '__all__'


class BlogTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogTag
        fields = '__all__'

class NewsletterEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsletterEmail 
        fields = '__all__'