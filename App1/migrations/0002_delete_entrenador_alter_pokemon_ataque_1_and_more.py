# Generated by Django 4.0.5 on 2022-07-21 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entrenador',
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='ataque_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ataque_1', to='App1.ataque'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='ataque_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ataque_2', to='App1.ataque'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='ataque_3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ataque_3', to='App1.ataque'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='ataque_4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ataque_4', to='App1.ataque'),
        ),
    ]
