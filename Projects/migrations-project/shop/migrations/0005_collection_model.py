from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_category_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name="Title")),
            ]
        ),

        migrations.AddField(
            model_name='product',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=models.deletion.SET_NULL, related_name='products', to='shop.collection'),
        )
    ]