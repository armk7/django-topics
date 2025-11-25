import uuid


def generate_uuid(apps, schema_editor):
    Product = apps.get_model('shop', 'Product')
    for product in Product.objects.all():
        product.uuid = uuid.uuid4().hex[:12].upper()
        product.save(update_fields=["uuid"])