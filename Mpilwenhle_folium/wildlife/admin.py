# admin.py
from django.contrib import admin
from django.db.models import Q, Sum, F
from django.contrib.gis.admin import OSMGeoAdmin
from django.utils.html import format_html
from wildlife.models import Organisation, Property, PropertyType, Province, TaxonRank, Taxon, AnnualPopulation

class PropertyAdmin(OSMGeoAdmin):
    list_display = ('name', 'property_type', 'geometry', 'display_color')  # Include 'display_color' in list_display
    list_filter = ('property_type',)

    def get_marker_color(self, obj):
        return 'red' if obj.property_type.name == 'Private' else 'blue' if obj.property_type.name == 'Community' else 'black'

    def display_color(self, obj):
        color = 'red' if obj.property_type.name == 'Private' else 'blue' if obj.property_type.name == 'Community' else 'black'
        return format_html(
            '<div style="width: 20px; height: 20px; border: 2px solid {}; background-color: {};"></div>',
            color,
            color
        )
    display_color.short_description = 'Property Color'

    # Add other settings for the map
    settings_overrides = {
        'DEFAULT_CENTER': (-29.873888, 30.961568),  # Adjust this to the center of your map
        'DEFAULT_ZOOM': 10,
        'MIN_ZOOM': 3,
        'MAX_ZOOM': 18,
        'SCALE': 'metric',
    }

admin.site.register(Organisation)
admin.site.register(PropertyType)
admin.site.register(Property, PropertyAdmin)  

class ProvinceAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(Q(organisation__isnull=False) | Q(property__isnull=False)).distinct()

admin.site.register(Province, ProvinceAdmin)  