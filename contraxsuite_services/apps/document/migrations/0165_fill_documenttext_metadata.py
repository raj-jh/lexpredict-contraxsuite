# Generated by Django 2.2 on 2019-07-10 13:14

from django.db import migrations, connection
from apps.common.utils import dictfetchall


def do_migrate(apps, schema_editor):
    with connection.cursor() as cursor:
        cursor.execute('INSERT INTO document_documenttext (document_id, full_text) SELECT id as document_id, full_text FROM document_document')

    with connection.cursor() as cursor:
        cursor.execute('INSERT INTO document_documentmetadata (document_id, metadata) SELECT id as document_id, metadata FROM document_document')


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0164_auto_20191107_0831'),
    ]

    operations = [
        migrations.RunPython(do_migrate, reverse_code=migrations.RunPython.noop),
    ]
