import json
import random

from django import template
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.html import conditional_escape, escape, format_html





register = template.Library()


@register.inclusion_tag('modal_list.html')
def cove_modal_list(**kw):
    return kw


@register.inclusion_tag('modal_errors.html')
def cove_modal_errors(**context):
    if hasattr(settings, 'VALIDATION_ERROR_LOCATIONS_LENGTH'):
        context['validation_error_locations_length'] = settings.VALIDATION_ERROR_LOCATIONS_LENGTH
    else:
        context['validation_error_locations_length'] = 1000
    if hasattr(settings, 'VALIDATION_ERROR_LOCATIONS_SAMPLE'):
        context['validation_error_locations_sample'] = settings.VALIDATION_ERROR_LOCATIONS_SAMPLE
    return context


@register.filter(name='json_decode')
def json_decode(error_json):
    return json.loads(error_json)


@register.filter(name='concat')
def concat(arg1, arg2):
    return str(arg1) + str(arg2)


@register.filter
def subtract(value, arg):
    return value - arg


@register.filter(name='sample')
def sample(population, k):
    return random.sample(population, k)


@register.filter(name='take_or_sample')
def take_or_sample(population, k):
    if hasattr(settings, 'VALIDATION_ERROR_LOCATIONS_SAMPLE') and settings.VALIDATION_ERROR_LOCATIONS_SAMPLE:
        if len(population) > k:
            return random.sample(population, k)
        else:
            return population
    else:
        return population[:k]


@register.filter(name='list_from_attribute')
def list_from_attribute(list_of_dicts, key_name):
    return [value[key_name] for value in list_of_dicts]



# These are "safe" html that we trust
# Don't insert any values into these strings without ensuring escaping
# e.g. using django's format_html function.
validation_error_template_lookup_safe = {
    "date-time": _("Date is not in the correct format"),
    "uri": _("Invalid 'uri' found"),
    "string": _("{}<code>{}</code> is not a string. Check that the value {} has quotes at the start and end. Escape any quotes in the value with <code>\</code>"),
    "integer": _("{}<code>{}</code> is not a integer. Check that the value {} doesn’t contain decimal points or any characters other than 0-9. Integer values should not be in quotes. "),
    "number": _("{}<code>{}</code> is not a number. Check that the value {} doesn’t contain any characters other than 0-9 and dot (<code>.</code>). Number values should not be in quotes. "),
    "object": _("{}<code>{}</code> is not a JSON object"),
    "array": _("{}<code>{}</code> is not a JSON array"),
}


@register.filter(name='html_error_msg')
def html_error_msg(error):
    # This should not happen for json schema validation, but may happen for
    # other forms of validation, e.g. XML for IATI
    if "validator" not in error:
        return error["message"]

    # Support cove-ocds, which hasn't fully moved over to the template tag based approach
    if "message_safe" in error and error["message_safe"] != escape(error["message"]):
        return format_html(error["message_safe"])

    e_validator = error['validator']
    e_validator_value = error.get('validator_value')
    validator_type = error['message_type']
    null_clause = error['null_clause']
    header = error['header_extra']

    if '[number]' in header:
        pre_header = _("Array Element ")
    else:
        pre_header = ""

    null_clause = ""
    if e_validator in ("format", "type"):
        if isinstance(e_validator_value, list):
            if "null" not in e_validator_value:
                null_clause = _("is not null, and")
        else:
            null_clause = _("is not null, and")

        message_safe_template = validation_error_template_lookup_safe.get(
            validator_type
        )

        return format_html(
            message_safe_template, pre_header, error['header'], null_clause
        )


    if e_validator == "required":
        path_no_number = error["path_no_number"].split("/")
        if len(path_no_number) > 1:
            parent_name = path_no_number[-1]
            return format_html(
                _("<code>{}</code> is missing but required within <code>{}</code>"),
                error["header"],
                parent_name,
            )
        else:
            return format_html(
                _("<code>{}</code> is missing but required"), error["header"]
            )

    if e_validator == "enum":
        return format_html(_("Invalid code found in <code>{}</code>"), header)

    if e_validator == "pattern":
        return format_html(
            _("<code>{}</code> does not match the regex <code>{}</code>"),
            header,
            e_validator_value,
        )

    if e_validator == "minItems" and e_validator_value == 1:
        return format_html(
            _("<code>{}</code> is too short. You must supply at least one value, or remove the item entirely (unless it’s required)."),
            error.get("instance"),
        )

    if e_validator == "minLength" and e_validator_value == 1:
        return format_html(
            _('<code>"{}"</code> is too short. Strings must be at least one character. This error typically indicates a missing value.'),
            error.get("instance"),
        )

    if e_validator == "minProperties":
        return _("{} does not have enough properties").format(error.get("instance"))


    if error.get("error_id"):
        if error["error_id"] == "uniqueItems_no_ids":
            return _("Array has non-unique elements")
        if error["error_id"].startswith("uniqueItems_with_"):
            id_name = error["error_id"][len("uniqueItems_with_"):]
            return _("Non-unique {} values").format(id_name)


    return error["message"]
