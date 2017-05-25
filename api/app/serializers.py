from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'college')

    def validate_last_name(self, data):
        val = self.initial_data['first_name']
        first_flag = False
        last_flag = False
        for i in val:
            for j in 'aeiouAEIOU':
                if i==j:
                    first_flag = True
                    break
        for i in data:
            for j in 'aeiouAEIOU':
                if i==j:
                    last_flag = True
                    break
        if first_flag != last_flag:
            raise serializers.ValidationError("Both first name and last name should contain vowels")
        return data