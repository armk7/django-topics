from django.db import migrations, models
import uuid

def generate_uuids(apps, schema_editor):
    Product = apps.get_model('shop', 'Product')
    for product in Product.objects.filter(uuid__isnull=True):
        product.uuid = uuid.uuid4()
        product.save(update_fields=['uuid'])

class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_previous_migration'),
    ]

    operations = [
        migrations.RunPython(generate_uuids, migrations.RunPython.noop),
    ]
