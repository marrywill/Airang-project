from rest_framework import serializers

from .models import *


class StoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'


class MyStoryCreateRequestSerializer(serializers.Serializer):
    story_id = serializers.IntegerField()
    story_name = serializers.CharField()


class MyStoryCreateSerializer(serializers.ModelSerializer):
    finished = serializers.IntegerField(required=False)
    class Meta:
        model = MyStory
        fields = (
            'story_name',
            'story',
            'user',
            'finished',
            'is_default',
        )


class MyStoryAddMyStorySerializer(serializers.Serializer):
    class Meta:
        model = MyStory
        fields = ('mystory')


class MyStoryAddRequestSerializer(serializers.Serializer):
    substory_list = serializers.ListField()
    
        
class CharacterOfScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            'id',
            'name',
            'thumbnail',
        )


class ScriptSerializer(serializers.ModelSerializer):
    character = CharacterOfScriptSerializer()
    class Meta:
        model = Script
        fields = (
            'id',
            'character',
            'order',
            'content',
            'substory',
            'has_name',
        )


class StoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryImage
        fields = '__all__'


class SubstorySerializer(serializers.ModelSerializer):
    scripts = ScriptSerializer(many=True)
    images = StoryImageSerializer(many=True)
    class Meta:
        model = Substory
        fields = (
            'id',
            'next_id',
            'has_branch',
            'scripts',
            'images',
            'back_image',
        )


class MySubstorySerializer(serializers.ModelSerializer):
    substory = SubstorySerializer()
    class Meta:
        model = MySubstory
        fields = '__all__'


class MySubstoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySubstory
        fields = '__all__'


class BranchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        depth = 1
        fields = (
            'id',
            'question',
            'selects',
            'left_image',
            'right_image',
        )

class MyCharacterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCharacter
        fields = (
            'character',
            'family',
        )


class MyCharacterBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCharacter
        depth = 1
        fields = (
            'id',
            'family'
        )


class MyCharacterSerializer(serializers.ModelSerializer):
    class Meta(MyCharacterCreateSerializer.Meta):
        depth = 1
        fields = MyCharacterCreateSerializer.Meta.fields + ('id',)


class MyStorySerializer(serializers.ModelSerializer):
    mystory = MySubstorySerializer()
    class Meta:
        model = MyStory
        depth = 1
        fields = (
            'id',
            'user',
            'created',
            'story',
            'story_name',
            'mystory',
            'mycharacters',
            'finished',
            'is_default',
        )


class MySubstoryDetailSerializer(serializers.ModelSerializer):
    substory = SubstorySerializer()
    class Meta:
        model = MySubstory
        fields = (
            'id',
            'next_id',
            'is_end',
            'substory'
        )
