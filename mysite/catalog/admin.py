from django.contrib import admin
from django.shortcuts import render
from .models import Attribute, Product, ContactFormPage

class DoubleConfirmAdmin(admin.ModelAdmin):
    def delete_view(self, request, object_id, extra_context=None):
        if request.POST.get("confirm_stage") == "second":
            return super().delete_view(request, object_id, extra_context)
        if request.method == "POST":
            obj = self.get_object(request, object_id)
            context = {
                **(extra_context or {}),
                "object": obj,
                "confirm_stage": "second",
            }
            return render(request, "admin/double_confirm_delete.html", context)
        return super().delete_view(request, object_id, extra_context)

@admin.register(Attribute)
class AttributeAdmin(DoubleConfirmAdmin):
    list_display = ["name"]

@admin.register(Product)
class ProductAdmin(DoubleConfirmAdmin):
    list_display = ["name"]
    filter_horizontal = ["attributes"]

@admin.register(ContactFormPage)
class ContactFormPageAdmin(DoubleConfirmAdmin):
    list_display = ["title"]
