from django.db.models import F
from rest_framework import serializers
from ..models import Position, Manager, MessengerPlatform, Contact, Partner, ManagerPosition


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
    managers = BaseManagerSerializer(many=True)

    def to_representation(self, instance):
        ordered_managers = Manager.objects.filter(managerposition__position=instance).annotate(
            order_value=F('managerposition__order_manager_position')
        ).order_by('order_value')
        instance.managers = ordered_managers
        return super().to_representation(instance)

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
