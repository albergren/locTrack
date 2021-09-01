from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):

#    parent_category = serializers.SerializerMethodField()
    print("sdlkfjsdlkjfsldkjflskdjflkj")
    class Meta:
        model = Category
        fields = '__all__'
                  
    def get_parent(self, obj):
        if obj.parent_category is not None:
            print("-------------------------------------")
            return CategorySerializer(obj.parent_category).data
        else:
            None
