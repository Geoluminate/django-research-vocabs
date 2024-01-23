from django.contrib import admin
from django.utils.safestring import mark_safe as marksafe

from research_vocabs.models import Concept

from .models import ExampleModel

admin.site.register(ExampleModel, admin.ModelAdmin)


@admin.register(Concept)
class ConceptAdmin(admin.ModelAdmin):
    list_display = [
        "label",
        "URI_display",
        "scheme_display",
        "tag_count",
    ]
    list_filter = [
        "scheme_label",
    ]

    def URI_display(self, obj):
        return marksafe(f"<a href='{obj.URI}'>{obj.URI}</a>")

    URI_display.short_description = "Label"

    def scheme_display(self, obj):
        return marksafe(f"<a href='{obj.scheme_URI}'>{obj.scheme_label}</a>")

    scheme_display.short_description = "Scheme"

    def tag_count(self, obj):
        return obj.research_vocabs_taggedconcept_items.count()
