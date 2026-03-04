# Generated manually for initial funds model.

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('risk_level', models.CharField(max_length=200)),
                ('expense_ratio', models.CharField(max_length=200)),
                ('returns_1yr', models.CharField(max_length=200)),
                ('returns_3yr', models.CharField(max_length=200)),
            ],
        ),
    ]
