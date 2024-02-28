from django.contrib.admin import SimpleListFilter
from django.utils.translation import gettext_lazy


class DonorBusinessFilter(SimpleListFilter):
    title = gettext_lazy('Donor Type')
    parameter_name = 'donor_type'

    def lookups(self, request, model_admin):
        return (
            ('1', gettext_lazy('Business')),
            ('0', gettext_lazy('Individual'))
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.are_businesses()
        elif self.value() == '0':
            return queryset.are_individuals()
        return queryset
