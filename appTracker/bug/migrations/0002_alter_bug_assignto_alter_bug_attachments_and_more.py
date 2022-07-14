# Generated by Django 4.0.5 on 2022-07-12 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='assignTo',
            field=models.CharField(max_length=34),
        ),
        migrations.AlterField(
            model_name='bug',
            name='attachments',
            field=models.FileField(upload_to='Media'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='bugType',
            field=models.CharField(choices=[('graphic', 'Graphic'), ('text', 'Text'), ('navigation', 'Navigation')], max_length=12),
        ),
        migrations.AlterField(
            model_name='bug',
            name='priorityLevel',
            field=models.CharField(choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], default='C', max_length=1),
        ),
        migrations.AlterField(
            model_name='bug',
            name='status',
            field=models.CharField(choices=[('assigned', 'Assigned'), ('acknowledged', 'Acknowledged'), ('feedback', 'Feedback'), ('resolved', 'Resolved'), ('closed', 'Closed')], default='assigned', max_length=12),
        ),
    ]
