# Generated manually for initial advisors model.

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('expertise', models.CharField(max_length=200)),
                ('experience_years', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
