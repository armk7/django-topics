import uuid


def generate_uuid(apps, schema_editor):
    Product = apps.get_model('shop', 'Product')
    for product in Product.objects.all():
        product.uuid = uuid.uuid4()
        product.save()


# another way:
# this is not used yet
def generate_uuids_0(apps, schema_editor):
    Product = apps.get_model('shop', 'Product')
    import uuid
    for obj in Product.objects.filter(uuid__isnull=True):
        Product.objects.filter(pk=obj.pk).update(uuid=uuid.uuid4())
