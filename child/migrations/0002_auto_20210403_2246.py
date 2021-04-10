# Generated by Django 3.0.5 on 2021-04-03 19:46

import child.models
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20210403_2034'),
        ('child', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='childdata',
            name='guardian',
        ),
        migrations.AddField(
            model_name='childdata',
            name='Courses',
            field=djongo.models.fields.ArrayReferenceField(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.CourseData'),
        ),
        migrations.AddField(
            model_name='childdata',
            name='guardian_email_address',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='childdata',
            name='guardian_first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='childdata',
            name='guardian_last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='childdata',
            name='subjects',
            field=djongo.models.fields.ArrayField(model_container=child.models.Subject, null=True),
        ),
        migrations.AlterField(
            model_name='childdata',
            name='about_user',
            field=models.TextField(max_length=500),
        ),
    ]
