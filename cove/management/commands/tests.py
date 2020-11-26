import os

import pytest
from django.core.files.base import ContentFile
from django.core.management import call_command
from django.utils import timezone

from cove.input.models import SuppliedData


@pytest.mark.django_db
def test_expire_files():
    recent = SuppliedData.objects.create()
    recent.original_file.save("test.json", ContentFile("{}"))

    old = SuppliedData.objects.create()
    old.created = timezone.datetime(2015, 1, 1)
    old.original_file.save("test.json", ContentFile("{}"))

    call_command("expire_files")
    assert os.path.exists(recent.upload_dir())
    assert not os.path.exists(old.upload_dir())
