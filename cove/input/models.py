from urllib.parse import urlsplit
from django.db import models
import uuid
from django.urls import reverse
import os
from django.conf import settings
import requests
from django.core.files.base import ContentFile
from werkzeug.http import parse_options_header
import secrets
import string

CONTENT_TYPE_MAP = {
    'application/json': 'json',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': 'xlsx',
    'text/csv': 'csv',
    'application/vnd.oasis.opendocument.spreadsheet': 'ods',
    'application/xml': 'xml',
    'text/xml': 'xml',
}


def upload_to(instance, filename=''):
    alphabet = string.ascii_letters + string.digits
    random_string = "".join(secrets.choice(alphabet) for i in range(16))
    return os.path.join(str(instance.pk), random_string, filename)


class SuppliedData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    source_url = models.URLField(null=True, max_length=2000)
    original_file = models.FileField(upload_to=upload_to, max_length=256)
    current_app = models.CharField(max_length=20)

    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    rendered = models.BooleanField(default=False)

    # Last schema version applied to the stored data
    schema_version = models.CharField(max_length=10, default='')
    # Schema version in uploaded/linked file
    data_schema_version = models.CharField(max_length=10, default='')

    # Parameters that were passed for this supplied data
    parameters = models.TextField(blank=True, null=True)


    form_name = models.CharField(
        max_length=20,
        choices=[
            ('upload_form', 'File upload'),
            ('url_form', 'Downloaded from URL'),
            ('text_form', 'Pasted into textarea'),
        ],
        null=True
    )

    def get_absolute_url(self):
        return reverse('explore', args=(self.pk,), current_app=self.current_app)

    def upload_dir(self):
        return os.path.join(settings.MEDIA_ROOT, str(self.pk), '')

    def upload_url(self):
        return os.path.join(settings.MEDIA_URL, str(self.pk), '')

    def is_google_doc(self):
        return self.source_url.startswith('https://docs.google.com/')

    def download(self):
        if self.source_url:
            r = requests.get(self.source_url, headers={'User-Agent': 'Cove (cove.opendataservice.coop)'})
            r.raise_for_status()
            content_type = r.headers.get('content-type', '').split(';')[0].lower()
            file_extension = CONTENT_TYPE_MAP.get(content_type)

            if not file_extension:
                _, options = parse_options_header(r.headers.get('content-disposition'))
                if 'filename*' in options:
                    filename = options['filename*']
                elif 'filename' in options:
                    filename = options['filename']
                else:
                    filename = urlsplit(r.url).path.rstrip('/').rsplit('/')[-1]
                possible_extension = filename.rsplit('.')[-1]
                if possible_extension in CONTENT_TYPE_MAP.values():
                    file_extension = possible_extension

            file_name = r.url.split('/')[-1].split('?')[0][:100]
            if file_name == '':
                file_name = 'file'
            if file_extension:
                if not file_name.endswith(file_extension):
                    file_name = file_name + '.' + file_extension
            self.original_file.save(
                file_name,
                ContentFile(r.content))
        else:
            raise ValueError('No source_url specified.')

    def __repr__(self):
        return "<SuppliedData source_url={} original_file.name={}>".format(
            repr(self.source_url),
            repr(self.original_file.name))
