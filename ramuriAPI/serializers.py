from django.contrib.auth.models import User, Group
from ramuriAPI.models import *
from rest_framework import serializers

class BrandSerializer(serializers.ModelSerializer):
    """ Serializer for brands.
    """
    class Meta:
        model = Brand
        fields = '__all__'
    
    environment_rating = serializers.SerializerMethodField()
    social_responsibility_rating = serializers.SerializerMethodField()
    animal_welfare_rating = serializers.SerializerMethodField()
    transparency_rating = serializers.SerializerMethodField()

    planet_goy_rating = serializers.SerializerMethodField()
    people_goy_rating = serializers.SerializerMethodField()
    animal_goy_rating = serializers.SerializerMethodField()

    def get_environment_rating(self, obj):
        """Environment rating is calculated from 100% GOY planet rating.
        GOY rating is out of 5 but shown rating is out of 10."""
        if obj.planet_goy_rating:
            return obj.planet_goy_rating * 1
        return 0
    
    def get_social_responsibility_rating(self, obj):
        """Social Responsibility rating is calculated from 100% GOY people rating.
        GOY rating is out of 5 but shown rating is out of 10."""
        if obj.people_goy_rating:
            return obj.people_goy_rating * 1
        return 0
    
    def get_animal_welfare_rating(self, obj):
        """Animal Welfare rating is calculated from 100% GOY animal rating.
        GOY rating is out of 5 but shown rating is out of 10."""
        if obj.animal_goy_rating:
            return obj.animal_goy_rating * 1
        return 0
    
    def get_transparency_rating(self, obj):
        """Transparency rating is an average of FTI ratings.
        Shown rating is out of 10.
        
        Assume that either has all FTI ratings or all are null.

        """
        if obj.policy_fti_rating:
            avg_fti = (obj.policy_fti_rating + obj.governance_fti_rating + obj.knowshow_fti_rating + \
            obj.spotlight_fti_rating + obj.traceability_fti_rating)/5
        else:
            avg_fti = 0
        return avg_fti
    
    def get_planet_goy_rating(self, obj):
        """GOY rating is inserted as out of 10 so divide by two"""
        if obj.planet_goy_rating:
            return obj.planet_goy_rating / 2
        return 0
    
    def get_people_goy_rating(self, obj):
        """GOY rating is inserted as out of 10 so divide by two"""
        if obj.people_goy_rating:
            return obj.people_goy_rating / 2
        return 0
    
    def get_animal_goy_rating(self, obj):
        """GOY rating is inserted as out of 10 so divide by two"""
        if obj.animal_goy_rating:
            return obj.animal_goy_rating / 2
        return 0

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
    


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']