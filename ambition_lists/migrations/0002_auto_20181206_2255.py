# Generated by Django 2.1.3 on 2018-12-06 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("ambition_lists", "0001_initial")]

    operations = [
        migrations.AlterModelOptions(
            name="abnormalresultsreason",
            options={"ordering": ["display_index", "name"]},
        ),
        migrations.AlterModelOptions(
            name="antibiotic", options={"ordering": ["display_index", "name"]}
        ),
        migrations.AlterModelOptions(
            name="cxrtype", options={"ordering": ["display_index", "name"]}
        ),
        migrations.AlterModelOptions(
            name="day14medication", options={"ordering": ["display_index", "name"]}
        ),
        migrations.AlterModelOptions(
            name="medication", options={"ordering": ["display_index", "name"]}
        ),
        migrations.AlterModelOptions(
            name="neurological", options={"ordering": ["display_index", "name"]}
        ),
        migrations.AlterModelOptions(
            name="otherdrug", options={"ordering": ["display_index", "name"]}
        ),
        migrations.AlterModelOptions(
            name="significantnewdiagnosis",
            options={"ordering": ["display_index", "name"]},
        ),
        migrations.AlterModelOptions(
            name="symptom", options={"ordering": ["display_index", "name"]}
        ),
    ]
