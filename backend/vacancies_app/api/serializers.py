from rest_framework import serializers
from ..models import Position, Manager, MessengerPlatform, Contact, Partner


class MessengerPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessengerPlatform
        fields = ('id', 'name', 'logo')


class ContactSerializer(serializers.ModelSerializer):
    messenger_platforms = MessengerPlatformSerializer(many=True)

    class Meta:
        model = Contact
        fields = ('id', 'phone', 'messenger_platforms')


class BaseManagerSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)

    class Meta:
        model = Manager
        fields = ('id', 'name', 'photo', 'facebook', 'contacts')


class PositionSerializer(serializers.ModelSerializer):
    managers = BaseManagerSerializer(many=True, source='manager_set')

    class Meta:
        model = Position
        lookup_field = 'slug'
        fields = ('id', 'slug', 'name', 'important', 'picture', 'salary', 'location', 'note', 'short_description', 'description', 'managers')


class PositionSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'name', 'slug', 'location')


class ManagerSerializer(BaseManagerSerializer):
    positions = PositionSummarySerializer(many=True)

    class Meta(BaseManagerSerializer.Meta):
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ('name', 'link', 'picture',)
