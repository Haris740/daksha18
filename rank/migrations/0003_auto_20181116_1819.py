# Generated by Django 2.1.3 on 2018-11-16 18:19

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0002_auto_20181116_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='events',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('kadaprasangham', 'KADHAPRASANGAM'), ('monoact', 'MONOACT'), ('western_solo', 'WESTERN SOLO'), ('mappila', 'MAPPILAPATTU'), ('mimicry', 'MIMICRY'), ('naadoodinritham', 'NAADODINIRTHAM'), ('ottamthulla', 'OTTANTHULLAL'), ('bharathanatyam', 'BHARATHANATYAM'), ('mohiniyattam', 'MOHINIYATTAM'), ('speech_eng', 'SPEECH ENGLISH'), ('speech_mal', 'SPEECH MALAYALAM'), ('speech_hin', 'SPEECH HINDI'), ('violin', 'VIOLIN'), ('veena', 'VEENA'), ('organ', 'ORGAN'), ('thabala', 'THABALA'), ('guitar', 'GUITAR'), ('mrithangam', 'MRITHANGAM'), ('kavitha_mal', 'KAVITHA MALAYALAM'), ('poem_eng', 'POEM ENGLISH'), ('poem_hin', 'POEM HINDI'), ('poem_arab', 'POEM ARABIC'), ('poem_sanskrit', 'POEM SANSKRIT'), ('lightmusic', 'LIGHT MUSIC'), ('classic_music', 'CLASSICAL MUSIC')], default='KADHAPRASANGAM', max_length=264),
        ),
    ]
