from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(
                choices=[('ADMIN', 'Admin'), ('INVESTOR', 'Investor'), ('ADVISOR', 'Advisor')],
                default='INVESTOR',
                max_length=20,
            ),
        ),
    ]
