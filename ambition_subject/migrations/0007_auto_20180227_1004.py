# Generated by Django 2.0.2 on 2018-02-27 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("ambition_subject", "0006_auto_20180227_0953")]

    operations = [
        migrations.AlterField(
            model_name="historicallumbarpuncturecsf",
            name="csf_cr_ag_lfa",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                max_length=5,
                verbose_name="CSF CrAg done by IMMY CrAg LFA:",
            ),
        ),
        migrations.AlterField(
            model_name="lumbarpuncturecsf",
            name="csf_cr_ag_lfa",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="N/A",
                max_length=5,
                verbose_name="CSF CrAg done by IMMY CrAg LFA:",
            ),
        ),
    ]