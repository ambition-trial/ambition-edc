# Generated by Django 2.1 on 2018-09-06 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("ambition_ae", "0009_auto_20180901_1512")]

    operations = [
        migrations.AlterField(
            model_name="aeinitial",
            name="ambisome_relation",
            field=models.CharField(
                choices=[
                    ("not_related", "Not related"),
                    ("unlikely_related", "Unlikely related"),
                    ("possibly_related", "Possibly related"),
                    ("probably_related", "Probably related"),
                    ("definitely_related", "Definitely related"),
                    ("N/A", "Not applicable"),
                ],
                editable=False,
                max_length=25,
                null=True,
                verbose_name="Relationship to Ambisome:",
            ),
        ),
        migrations.AlterField(
            model_name="aeinitial",
            name="amphotericin_b_relation",
            field=models.CharField(
                choices=[
                    ("not_related", "Not related"),
                    ("unlikely_related", "Unlikely related"),
                    ("possibly_related", "Possibly related"),
                    ("probably_related", "Probably related"),
                    ("definitely_related", "Definitely related"),
                    ("N/A", "Not applicable"),
                ],
                editable=False,
                max_length=25,
                null=True,
                verbose_name="Relationship to Amphotericin B:",
            ),
        ),
        migrations.AlterField(
            model_name="aeinitial",
            name="amphotericin_relation",
            field=models.CharField(
                choices=[
                    ("not_related", "Not related"),
                    ("unlikely_related", "Unlikely related"),
                    ("possibly_related", "Possibly related"),
                    ("probably_related", "Probably related"),
                    ("definitely_related", "Definitely related"),
                    ("N/A", "Not applicable"),
                ],
                max_length=25,
                null=True,
                verbose_name="Amphotericin formulation:",
            ),
        ),
        migrations.AlterField(
            model_name="aeinitial",
            name="fluconazole_relation",
            field=models.CharField(
                choices=[
                    ("not_related", "Not related"),
                    ("unlikely_related", "Unlikely related"),
                    ("possibly_related", "Possibly related"),
                    ("probably_related", "Probably related"),
                    ("definitely_related", "Definitely related"),
                    ("N/A", "Not applicable"),
                ],
                max_length=25,
                verbose_name="Relationship to Fluconozole:",
            ),
        ),
        migrations.AlterField(
            model_name="aeinitial",
            name="flucytosine_relation",
            field=models.CharField(
                choices=[
                    ("not_related", "Not related"),
                    ("unlikely_related", "Unlikely related"),
                    ("possibly_related", "Possibly related"),
                    ("probably_related", "Probably related"),
                    ("definitely_related", "Definitely related"),
                    ("N/A", "Not applicable"),
                ],
                max_length=25,
                verbose_name="Relationship to Flucytosine:",
            ),
        ),
        migrations.AlterField(
            model_name="historicalaeinitial",
            name="ambisome_relation",
            field=models.CharField(
                choices=[
                    ("not_related", "Not related"),
                    ("unlikely_related", "Unlikely related"),
                    ("possibly_related", "Possibly related"),
                    ("probably_related", "Probably related"),
                    ("definitely_related", "Definitely related"),
                    ("N/A", "Not applicable"),
                ],
                editable=False,
                max_length=25,
                null=True,
                verbose_name="Relationship to Ambisome:",
            ),
        ),
        migrations.AlterField(
            model_name="historicalaeinitial",
            name="amphotericin_b_relation",
            field=models.CharField(
                choices=[
                    ("not_related", "Not related"),
                    ("unlikely_related", "Unlikely related"),
                    ("possibly_related", "Possibly related"),
                    ("probably_related", "Probably related"),
                    ("definitely_related", "Definitely related"),
                    ("N/A", "Not applicable"),
                ],
                editable=False,
                max_length=25,
                null=True,
                verbose_name="Relationship to Amphotericin B:",
            ),
        ),
        migrations.AlterField(
            model_name="historicalaeinitial",
            name="amphotericin_relation",
            field=models.CharField(
                choices=[
                    ("not_related", "Not related"),
                    ("unlikely_related", "Unlikely related"),
                    ("possibly_related", "Possibly related"),
                    ("probably_related", "Probably related"),
                    ("definitely_related", "Definitely related"),
                    ("N/A", "Not applicable"),
                ],
                max_length=25,
                null=True,
                verbose_name="Amphotericin formulation:",
            ),
        ),
        migrations.AlterField(
            model_name="historicalaeinitial",
            name="fluconazole_relation",
            field=models.CharField(
                choices=[
                    ("not_related", "Not related"),
                    ("unlikely_related", "Unlikely related"),
                    ("possibly_related", "Possibly related"),
                    ("probably_related", "Probably related"),
                    ("definitely_related", "Definitely related"),
                    ("N/A", "Not applicable"),
                ],
                max_length=25,
                verbose_name="Relationship to Fluconozole:",
            ),
        ),
        migrations.AlterField(
            model_name="historicalaeinitial",
            name="flucytosine_relation",
            field=models.CharField(
                choices=[
                    ("not_related", "Not related"),
                    ("unlikely_related", "Unlikely related"),
                    ("possibly_related", "Possibly related"),
                    ("probably_related", "Probably related"),
                    ("definitely_related", "Definitely related"),
                    ("N/A", "Not applicable"),
                ],
                max_length=25,
                verbose_name="Relationship to Flucytosine:",
            ),
        ),
    ]
