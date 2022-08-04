# Generated by Django 4.1 on 2022-08-04 07:55

from django.db import migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_loyiha'),
    ]

    operations = [
        migrations.AddField(
            model_name='loyiha',
            name='status',
            field=model_utils.fields.StatusField(choices=[('ishga_tushmagan', 'ishga_tushmagan'), ('ishga_tushmagan', 'ishga_tushmagan'), ('kredit_ajratilmagan', 'kredit_ajratilmagan'), ('svod', 'svod')], default='ishga_tushmagan', max_length=100, no_check_for_status=True),
        ),
    ]
