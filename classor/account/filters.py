import django_filters
from .models import Profile
from django.contrib.auth.models import User

class ProfileFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Profile
        fields= ['user',]
