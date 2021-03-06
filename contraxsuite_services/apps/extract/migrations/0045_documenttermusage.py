# Generated by Django 2.2.8 on 2020-01-28 11:16

from django.db import migrations, models, connection
import django.db.models.deletion


def sum_term_usage(apps, schema_editor):
    sql_cmd = '''
    INSERT INTO "extract_documenttermusage" ("document_id", "term_id", "count")
    SELECT "document_textunit"."document_id", "extract_termusage"."term_id", 
        SUM("extract_termusage"."count") AS "count" 
    FROM "extract_termusage" 
    INNER JOIN "document_textunit" ON ("extract_termusage"."text_unit_id" = "document_textunit"."id") 
    GROUP BY "document_textunit"."document_id", "extract_termusage"."term_id" ORDER BY "count" DESC;
    '''
    with connection.cursor() as cursor:
        cursor.execute(sql_cmd)


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0181_merge_20200123_2008'),
        ('extract', '0044_cache_locate_configs'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentTermUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(db_index=True, default=0)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.Document')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extract.Term')),
            ],
            options={
                'ordering': ['-count'],
                'unique_together': {('document', 'term')},
            },
        ),
        migrations.RunPython(sum_term_usage),
    ]
