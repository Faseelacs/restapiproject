# Generated by Django 3.2.11 on 2022-01-16 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0060_comment_topicandcomment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Topicandcomment',
        ),
    ]
