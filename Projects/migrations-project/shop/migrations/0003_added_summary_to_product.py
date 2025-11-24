from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_added_description_to_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.CharField(default='', max_length=160, verbose_name='Summary')
        ),
    ]