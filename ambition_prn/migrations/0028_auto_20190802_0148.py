# Generated by Django 2.2.2 on 2019-08-01 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("ambition_prn", "0027_auto_20190802_0137")]

    operations = [
        migrations.RenameField(
            model_name="deathreporttmg",
            old_name="cause_of_death",
            new_name="cause_of_death_old",
        ),
        migrations.RenameField(
            model_name="historicaldeathreporttmg",
            old_name="cause_of_death",
            new_name="cause_of_death_old",
        ),
        migrations.AddField(
            model_name="deathreporttmg",
            name="cause_of_death",
            field=models.ForeignKey(
                help_text="Main cause of death in the opinion of the local study doctor and local PI",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="edc_adverse_event.CauseOfDeath",
                verbose_name="Main cause of death",
            ),
        ),
        migrations.AddField(
            model_name="historicaldeathreporttmg",
            name="cause_of_death",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                help_text="Main cause of death in the opinion of the local study doctor and local PI",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="edc_adverse_event.CauseOfDeath",
                verbose_name="Main cause of death",
            ),
        ),
    ]