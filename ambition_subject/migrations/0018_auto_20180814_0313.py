# Generated by Django 2.1 on 2018-08-14 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("ambition_subject", "0017_auto_20180811_2329")]

    operations = [
        migrations.AlterModelOptions(
            name="subjectconsent",
            options={
                "get_latest_by": "consent_datetime",
                "ordering": ("created",),
                "permissions": (("can_display_consent", "Can display consent"),),
            },
        )
    ]
