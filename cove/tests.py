import copy
import pytest

from cove.views import get_file_name
from cove.templatetags.cove_tags import html_error_msg


def test_get_file_name_with_slash():
    file_name = get_file_name('c8291024-155a-46fa-8af2-0b6a30b4686c/file_name_with_slash.xml')

    assert file_name == 'file_name_with_slash.xml'


def test_get_file_name_without_slash():
    file_name = get_file_name('file_name_without_slash.xml')

    assert file_name == 'file_name_without_slash.xml'


def test_get_file_name_with_empty_string():
    file_name = get_file_name('')

    assert file_name == ''


def test_get_file_name_with_none():
    file_name = get_file_name(file_name=None)

    assert file_name is None


@pytest.mark.parametrize(
    "old_error",
    [
        {
            "error_id": None,
            "values": [{"path": "records/2/releases/0"}],
            "message": "'date' is missing but required within 'releases'",
            "header_extra": "releases/[number]",
            "message_type": "required",
            "validator": "required",
            "header": "date",
            "message_safe": "<code>date</code> is missing but required within <code>releases</code>",
            "null_clause": "",
            "path_no_number": "records/releases",
            "assumption": "embedded_releases",
        },
        {
            "error_id": None,
            "values": [
                {"path": "records/1/releases/0"},
                {"path": "records/3/releases/0"},
            ],
            "message": "'date' is missing but required within 'releases'",
            "header_extra": "releases/[number]",
            "message_type": "required",
            "validator": "required",
            "header": "date",
            "message_safe": "<code>date</code> is missing but required within <code>releases</code>",
            "null_clause": "",
            "path_no_number": "records/releases",
            "assumption": "linked_releases",
        },
        {
            "error_id": None,
            "values": [{"path": "releases/0"}, {"path": "releases/1"}],
            "message": "'id' is missing but required",
            "header_extra": "releases/[number]",
            "message_type": "required",
            "validator": "required",
            "header": "id",
            "message_safe": "<code>id</code> is missing but required",
            "null_clause": "",
            "path_no_number": "releases",
            "assumption": None,
        },
        {
            "error_id": None,
            "values": [{"path": "records/2/releases/0"}],
            "message": "'initiationType' is missing but required within 'releases'",
            "header_extra": "releases/[number]",
            "message_type": "required",
            "validator": "required",
            "header": "initiationType",
            "message_safe": "<code>initiationType</code> is missing but required within <code>releases</code>",
            "null_clause": "",
            "path_no_number": "records/releases",
            "assumption": "embedded_releases",
        },
        {
            "error_id": None,
            "values": [{"path": "records/0"}, {"path": "records/1"}],
            "message": "'ocid' is missing but required",
            "header_extra": "records/[number]",
            "message_type": "required",
            "validator": "required",
            "header": "ocid",
            "message_safe": "<code>ocid</code> is missing but required",
            "null_clause": "",
            "path_no_number": "records",
            "assumption": None,
        },
        {
            "error_id": None,
            "values": [{"path": "records/2/releases/0"}],
            "message": "'ocid' is missing but required within 'releases'",
            "header_extra": "releases/[number]",
            "message_type": "required",
            "validator": "required",
            "header": "ocid",
            "message_safe": "<code>ocid</code> is missing but required within <code>releases</code>",
            "null_clause": "",
            "path_no_number": "records/releases",
            "assumption": "embedded_releases",
        },
        {
            "error_id": None,
            "values": [
                {"value": "a string", "path": "records/6/releases"},
                {"value": None, "path": "records/7/releases"},
                {"path": "records/8/releases"},
            ],
            "message": "'releases' is not a JSON array",
            "header_extra": "releases",
            "message_type": "array",
            "validator": "type",
            "header": "releases",
            "message_safe": "<code>releases</code> is not a JSON array",
            "null_clause": "is not null, and",
            "path_no_number": "records/releases",
            "assumption": "linked_releases",
        },
        {
            "error_id": None,
            "values": [{"path": "records/2/releases/0"}],
            "message": "'tag' is missing but required within 'releases'",
            "header_extra": "releases/[number]",
            "message_type": "required",
            "validator": "required",
            "header": "tag",
            "message_safe": "<code>tag</code> is missing but required within <code>releases</code>",
            "null_clause": "",
            "path_no_number": "records/releases",
            "assumption": "embedded_releases",
        },
        {
            "error_id": None,
            "values": [{"path": "records/1/releases/0"}],
            "message": "'url' is missing but required within 'releases'",
            "header_extra": "releases/[number]",
            "message_type": "required",
            "validator": "required",
            "header": "url",
            "message_safe": "<code>url</code> is missing but required within <code>releases</code>",
            "null_clause": "",
            "path_no_number": "records/releases",
            "assumption": "linked_releases",
        },
        {
            "error_id": "uniqueItems_no_ids",
            "values": [{"path": "releases"}],
            "message": "Array has non-unique elements",
            "header_extra": "releases",
            "message_type": "uniqueItems",
            "validator": "uniqueItems",
            "header": "releases",
            "message_safe": "Array has non-unique elements",
            "null_clause": "",
            "path_no_number": "releases",
            "assumption": None,
        },
        {
            "error_id": "uniqueItems_with_id",
            "values": [
                {"value": "EXAMPLE-1-1", "path": "releases"},
                {"value": "EXAMPLE-1-2", "path": "releases"},
            ],
            "message": "Non-unique id values",
            "header_extra": "releases",
            "message_type": "uniqueItems",
            "validator": "uniqueItems",
            "header": "releases",
            "message_safe": "Non-unique id values",
            "null_clause": "",
            "path_no_number": "releases",
            "assumption": None,
        },
	{
	    "message": "Non-unique combination of ocid, id values",
	    "message_safe": "Non-unique combination of ocid, id values",
	    "validator": "uniqueItems",
	    "assumption": None,
	    "message_type": "uniqueItems",
	    "path_no_number": "releases",
	    "header": "releases",
	    "header_extra": "releases",
	    "null_clause": "",
	    "error_id": "uniqueItems_with_ocid__id",
	    "values": [
		{"path": "releases", "value": "EXAMPLE-1, EXAMPLE-1-1"},
		{"path": "releases", "value": "EXAMPLE-1, EXAMPLE-1-2"},
	    ],
	},
        {
            "error_id": "uniqueItems_with_id",
            "values": [
                {"value": "EXAMPLE-1-1", "path": "releases"},
                {"value": "EXAMPLE-1-2", "path": "releases"},
            ],
            "message": "Non-unique id values",
            "header_extra": "releases",
            "message_type": "uniqueItems",
            "validator": "uniqueItems",
            "header": "releases",
            "message_safe": "Non-unique id values",
            "null_clause": "",
            "path_no_number": "releases",
            "assumption": None,
        },
        {
            "error_id": None,
            "values": [{"path": "records/0/releases"}],
            "message": "[] is too short",
            "header_extra": "releases",
            "message_type": "minItems",
            "validator": "minItems",
            'validator_value': 1,
            "header": "releases",
            "message_safe": "<code>[]</code> is too short. You must supply at least one value, or remove the item entirely (unless it\u2019s required).",
            "null_clause": "",
            "path_no_number": "records/releases",
            "assumption": "linked_releases",
            "instance": [],
        },
    ],
)
def test_cove_tags_html_error_msg(old_error):
    html_msg = old_error["message_safe"]

    error = copy.copy(old_error)
    del error["message_safe"]

    assert html_error_msg(error) == html_msg
