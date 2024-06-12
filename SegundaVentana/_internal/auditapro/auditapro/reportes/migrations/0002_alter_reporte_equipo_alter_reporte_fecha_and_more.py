from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0001_initial'),  # Asegúrate de que el nombre de la migración aquí sea correcto
    ]

    operations = [
        migrations.AlterField(
            model_name='reporte',
            name='equipo',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='nombre',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
