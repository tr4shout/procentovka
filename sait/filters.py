import django_filters
from django_filters import CharFilter

from .models import Uni

#Создание фильтрации(поиска) по Университетам

class UniFilter(django_filters.FilterSet):
    tittle = CharFilter(field_name="tittle", lookup_expr="icontains")


    class Meta:
        model = Uni
        fields = "__all__"
        exclude = [
            "description",
            "number",
            "image",
            "title_ref",
            "ref",
        ]
