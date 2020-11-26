from os.path import split

from django.core.files import File
from django.core.management.base import BaseCommand

from cove.input.models import SuppliedData


class Command(BaseCommand):
    help = "Upload a file from the commandline, and return a Cove data url."

    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str)

    def handle(self, *args, file_name, **options):
        data = SuppliedData()
        head, tail = split(file_name)
        data.original_file.save(tail, File(open(file_name)))
        data.save()
        return data.get_absolute_url()
