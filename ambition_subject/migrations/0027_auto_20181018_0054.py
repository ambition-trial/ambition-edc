# Generated by Django 2.1 on 2018-10-17 22:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("ambition_subject", "0026_auto_20181018_0027")]

    operations = [
        migrations.AlterField(
            model_name="historicalpkpdcrf",
            name="flucytosine_dose_four",
            field=models.IntegerField(
                blank=True,
                help_text="Units in mg",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(9999),
                ],
                verbose_name="Flucytosine <u>DOSE&nbsp;4</u>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalpkpdcrf",
            name="flucytosine_dose_four_given",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=5,
                null=True,
                verbose_name="Flucytosine <b><u>DOSE&nbsp;4</u></b> given? ",
            ),
        ),
        migrations.AlterField(
            model_name="historicalpkpdcrf",
            name="flucytosine_dose_one",
            field=models.IntegerField(
                blank=True,
                help_text="Units in mg",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(9999),
                ],
                verbose_name="Flucytosine <u>DOSE&nbsp;1</u>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalpkpdcrf",
            name="flucytosine_dose_one_given",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=5,
                null=True,
                verbose_name="Flucytosine <b><u>DOSE&nbsp;1</u></b> given? ",
            ),
        ),
        migrations.AlterField(
            model_name="historicalpkpdcrf",
            name="flucytosine_dose_three",
            field=models.IntegerField(
                blank=True,
                help_text="Units in mg",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(9999),
                ],
                verbose_name="Flucytosine <u>DOSE&nbsp;3</u>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalpkpdcrf",
            name="flucytosine_dose_three_given",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=5,
                null=True,
                verbose_name="Flucytosine <b><u>DOSE&nbsp;3</u></b> given? ",
            ),
        ),
        migrations.AlterField(
            model_name="historicalpkpdcrf",
            name="flucytosine_dose_two",
            field=models.IntegerField(
                blank=True,
                help_text="Units in mg",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(9999),
                ],
                verbose_name="Flucytosine <u>DOSE&nbsp;2</u>",
            ),
        ),
        migrations.AlterField(
            model_name="historicalpkpdcrf",
            name="flucytosine_dose_two_given",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=5,
                null=True,
                verbose_name="Flucytosine <b><u>DOSE&nbsp;2</u></b> given? ",
            ),
        ),
        migrations.AlterField(
            model_name="historicalweek2",
            name="antibiotic_other",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="If other antibiotics, please specify:",
            ),
        ),
        migrations.AlterField(
            model_name="historicalweek2",
            name="drug_intervention_other",
            field=models.TextField(
                blank=True, null=True, verbose_name="If other, please specify:"
            ),
        ),
        migrations.AlterField(
            model_name="pkpdcrf",
            name="flucytosine_dose_four",
            field=models.IntegerField(
                blank=True,
                help_text="Units in mg",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(9999),
                ],
                verbose_name="Flucytosine <u>DOSE&nbsp;4</u>",
            ),
        ),
        migrations.AlterField(
            model_name="pkpdcrf",
            name="flucytosine_dose_four_given",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=5,
                null=True,
                verbose_name="Flucytosine <b><u>DOSE&nbsp;4</u></b> given? ",
            ),
        ),
        migrations.AlterField(
            model_name="pkpdcrf",
            name="flucytosine_dose_one",
            field=models.IntegerField(
                blank=True,
                help_text="Units in mg",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(9999),
                ],
                verbose_name="Flucytosine <u>DOSE&nbsp;1</u>",
            ),
        ),
        migrations.AlterField(
            model_name="pkpdcrf",
            name="flucytosine_dose_one_given",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=5,
                null=True,
                verbose_name="Flucytosine <b><u>DOSE&nbsp;1</u></b> given? ",
            ),
        ),
        migrations.AlterField(
            model_name="pkpdcrf",
            name="flucytosine_dose_three",
            field=models.IntegerField(
                blank=True,
                help_text="Units in mg",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(9999),
                ],
                verbose_name="Flucytosine <u>DOSE&nbsp;3</u>",
            ),
        ),
        migrations.AlterField(
            model_name="pkpdcrf",
            name="flucytosine_dose_three_given",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=5,
                null=True,
                verbose_name="Flucytosine <b><u>DOSE&nbsp;3</u></b> given? ",
            ),
        ),
        migrations.AlterField(
            model_name="pkpdcrf",
            name="flucytosine_dose_two",
            field=models.IntegerField(
                blank=True,
                help_text="Units in mg",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(9999),
                ],
                verbose_name="Flucytosine <u>DOSE&nbsp;2</u>",
            ),
        ),
        migrations.AlterField(
            model_name="pkpdcrf",
            name="flucytosine_dose_two_given",
            field=models.CharField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=5,
                null=True,
                verbose_name="Flucytosine <b><u>DOSE&nbsp;2</u></b> given? ",
            ),
        ),
        migrations.AlterField(
            model_name="week2",
            name="antibiotic_other",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="If other antibiotics, please specify:",
            ),
        ),
        migrations.AlterField(
            model_name="week2",
            name="drug_intervention_other",
            field=models.TextField(
                blank=True, null=True, verbose_name="If other, please specify:"
            ),
        ),
    ]
