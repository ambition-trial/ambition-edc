# Generated by Django 2.2 on 2019-05-05 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("ambition_prn", "0019_auto_20190316_2025")]

    operations = [
        migrations.AlterField(
            model_name="historicalstudyterminationconclusion",
            name="on_study_drug",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                max_length=25,
                verbose_name="Has the patient started 'study' drug",
            ),
        ),
        migrations.AlterField(
            model_name="studyterminationconclusion",
            name="on_study_drug",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                max_length=25,
                verbose_name="Has the patient started 'study' drug",
            ),
        ),
    ]
