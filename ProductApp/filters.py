import django_filters
from .models import Tv


class SnippetFilter(django_filters.FilterSet):
    # producent = django_filters.CharFilter(
    # field_name='producent' ,
    # lookup_expr='iexact', method='filter_by_producent'
    # )

    curved = django_filters.filters.ModelChoiceFilter(
        label='ddwdwdw', queryset=Tv.objects.filter(curved='True')
    )
    producent = django_filters.filters.BooleanFilter(label='ddwdwdw')

    class Meta:
        model = Tv
        fields = ['producent', 'promotion',
                  'diagonal', 'resolution',
                  'curved', 'refresh_rate',
                  'smart_tv', 'wifi'
                  ]

    def __init__(self, *args, **kwargs):
        super(SnippetFilter, self).__init__(*args, **kwargs)
        self.filters['curved'].label = "dwfdwdf"

    # def filter_by_producent(self, queryset, name, cattegory):
    #     return Tv.objects.filter(producent=name, cattegory=cattegory)
