from rest_framework import serializers

from vinipoonpn.users.models import User

# class UserSerializer(serializers.ModelSerializer[User]):
#     class Meta:
#         model = User
#         fields = ["username", "name", "url"]

#         extra_kwargs = {
#             "url": {"view_name": "api:user-detail", "lookup_field": "username"},
#         }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name"]
