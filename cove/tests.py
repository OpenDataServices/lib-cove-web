from cove.views import get_file_name

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