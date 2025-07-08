from django.shortcuts import render, get_object_or_404
from .models import Product, Attribute, ContactFormPage


def product_list(request):
    selected = request.GET.getlist('attribute')
    attributes = Attribute.objects.all()
    products = Product.objects.all()
    if selected:
        products = products.filter(attributes__id__in=selected).distinct()
    return render(
        request,
        "catalog/product_list.html",
        {
            "attributes": attributes,
            "selected": [int(s) for s in selected],
            "products": products,
        },
    )


def contact_form(request, pk):
    page = get_object_or_404(ContactFormPage, pk=pk)
    return render(request, "catalog/contact_form.html", {"page": page})
