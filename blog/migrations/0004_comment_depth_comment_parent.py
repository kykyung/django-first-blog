# Generated by Django 4.0.2 on 2022-02-04 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220119_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='depth',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_comments', to='blog.comment'),
        ),
    ]