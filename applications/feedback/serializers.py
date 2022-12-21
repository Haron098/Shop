from rest_framework import serializers
from applications.feedback.models import Comment, Favorite


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Comment
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Favorite
        fields = '__all__'

    # def to_representation(self, instance):
    #     favorite = super().to_representation(instance)
    #     return {'time'}
