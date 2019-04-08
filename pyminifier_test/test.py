# -*- coding: utf-8 -*-
import os, sys
import pytest
import tempfile
import shutil
import stat
from go_drive.util import fs_util, appdirs, temp_utils


is_osx = bool(sys.platform == 'darwin')
is_win = sys.platform.startswith('win')


# function level comment
def test_copy_to_temp_folder():
    """
    here's a doc string to see if it will get removed
    """

    with pytest.raises(Exception):
        fs_util.copy_to_temp_folder()

    with pytest.raises(Exception):
        fs_util.copy_to_temp_folder("gibberish_path.txt")

    tmp_file_path = fs_util.copy_to_temp_folder(__file__, suffix=".txt")
    assert os.path.exists(tmp_file_path)


### MORE COMMENTS
# Hello

def test_replace_folder():

    assert not fs_util.replace_folder("blah", "", True)

    with pytest.raises(Exception):
        fs_util.replace_folder("gibberish_path.txt", "")

    temp_dir = appdirs.get_temp_dir()

    dest_dir = tempfile.mkdtemp(prefix="replace_folder_dest_", dir=temp_dir)
    os.makedirs(dest_dir + "/dest_folder1/dest_folder2")

    src_dir_parent = tempfile.mkdtemp(prefix="replace_folder_src_", dir=temp_dir)
    src_dir = os.path.join(src_dir_parent, "src")
    os.makedirs(src_dir + "/src_folder1/src_folder2")

    fs_util.replace_folder(src_dir, dest_dir)

    dest_dir_backup = os.path.normpath(dest_dir + ".bak")

    assert not os.path.exists(src_dir)
    assert os.path.exists(dest_dir + "/src_folder1/src_folder2")
    assert not os.path.exists(dest_dir_backup)

    shutil.rmtree(src_dir_parent)
    shutil.rmtree(dest_dir)

    assert not os.path.exists(dest_dir)
    assert not os.path.exists(src_dir_parent)


def test_remove_file():

    assert fs_util.remove_file(None) is None


def test_remove_child_files_and_folders():

    temp_dir = appdirs.get_temp_dir()

    for i in range(10):
        sub_dir = temp_dir + "/" + str(i)
        os.mkdir(sub_dir)
        path = os.path.join(temp_dir, sub_dir)
        file_path = ""

        if i % 2 == 0:
            tmp_file = temp_utils.make_temporary_file("notes", dir=sub_dir)
            file_path = os.path.join(path, tmp_file)
            assert os.path.isfile(file_path)

        else:
            assert not os.path.isfile(file_path)

        if i % 3 == 0:
            fs_util.remove_child_files_and_folders(temp_dir)
            assert not os.path.exists(path)
            assert not os.path.isfile(file_path)

        else:
            assert os.path.exists(path)


def test_copy_file():
    temp_dir = appdirs.get_temp_dir()

    src = temp_utils.make_temporary_file("test", dir=temp_dir)
    dst = temp_utils.make_temporary_file("boo", dir=temp_dir)

    with pytest.raises(Exception):
        fs_util.copy_file(None, "blah")
    with pytest.raises(Exception):
        fs_util.copy_file("source", None)
    with pytest.raises(Exception):
        fs_util.copy_file("source", "dest")
    with pytest.raises(Exception):
        fs_util.copy_file(temp_dir, temp_dir + "/dest", False)

    fs_util.copy_file(src, dst)


def test_rename_file():
    temp_dir = appdirs.get_temp_dir()

    src = temp_utils.make_temporary_file("test", dir=temp_dir)
    dst = temp_utils.make_temporary_file("boo", dir=temp_dir)

    with pytest.raises(Exception):
        fs_util.rename_file(None, "blah")
    with pytest.raises(Exception):
        fs_util.rename_file("source", None)
    with pytest.raises(Exception):
        fs_util.rename_file("source", "dest")
    with pytest.raises(Exception):
        fs_util.rename_file(temp_dir, temp_dir + "/dest", False)

    fs_util.rename_file(src, dst)


def test_backup_folder():
    temp_dir = appdirs.get_temp_dir()
    dst_name = temp_dir + ".bak"

    # destination folder (already exists to trigger error below)
    os.mkdir(dst_name)

    file_src = temp_utils.make_temporary_file("test", dir=temp_dir)

    with pytest.raises(Exception):
        fs_util.backup_folder(None)
    with pytest.raises(Exception):
        fs_util.backup_folder(file_src)

    # backup dest already exists exception
    with pytest.raises(Exception):
        fs_util.backup_folder(temp_dir, ".bak", False)

    d1 = fs_util.backup_folder(temp_dir, ".bak")
    d2 = fs_util.backup_folder(temp_dir)
    pass


def test_rename_folder():
    temp_dir = appdirs.get_temp_dir()
    dst_name = temp_dir + temp_utils.make_random_name(5)
    os.mkdir(dst_name)

    file_dst = temp_utils.make_temporary_file("test", dir=dst_name)

    with pytest.raises(Exception):
        fs_util.rename_folder(None, "dest")
    with pytest.raises(Exception):
        fs_util.rename_folder(temp_dir, None)
    with pytest.raises(Exception):
        fs_util.rename_folder("fake_path/fake", dst_name)
    with pytest.raises(Exception):
        fs_util.rename_folder(temp_dir, file_dst)
    with pytest.raises(Exception):
        fs_util.rename_folder(temp_dir, dst_name, False)

    fs_util.rename_folder("fake_path/fake", dst_name, ignore_empty_src=True)
    fs_util.rename_folder(temp_dir, dst_name)


def test_copy_tree():
    temp_dir = appdirs.get_temp_dir()
    dst_name = temp_dir + temp_utils.make_random_name(5)
    path_temp = temp_dir + temp_utils.make_random_name(5)
    dst_name_2 = os.path.join(path_temp, temp_utils.make_random_name(3))

    os.mkdir(dst_name)

    file_src = temp_utils.make_temporary_file("test", dir=temp_dir)

    with pytest.raises(Exception):
        fs_util.copy_tree(None, "dest")
    with pytest.raises(Exception):
        fs_util.copy_tree(temp_dir, None)
    with pytest.raises(Exception):
        fs_util.copy_tree("source", "dest")
    with pytest.raises(Exception):
        fs_util.copy_tree(file_src, dst_name)
    with pytest.raises(Exception):
        fs_util.copy_tree(temp_dir, dst_name, False)
    with pytest.raises(Exception):
        fs_util.copy_tree(temp_dir, dst_name_2, create_parent=False)
    with pytest.raises(Exception):
        fs_util.copy_tree(temp_dir, '')

    fs_util.copy_tree(temp_dir, dst_name)
    pass


def test_rmtree():
    temp_dir = appdirs.get_temp_dir()
    sub_dir_1 = os.path.join(temp_dir, temp_utils.make_random_name(5))
    sub_dir_2 = os.path.join(temp_dir, temp_utils.make_random_name(5))
    sub_sub_dir = os.path.join(sub_dir_2, temp_utils.make_random_name(3))

    os.makedirs(sub_sub_dir)
    os.makedirs(sub_dir_1)

    assert os.path.isdir(sub_sub_dir)
    assert os.path.isdir(sub_dir_1)
    assert os.path.isdir(sub_dir_2)

    fs_util.rmtree(None)
    fs_util.rmtree("gibberish")
    fs_util.rmtree(temp_dir)

    assert not os.path.isdir(sub_sub_dir)
    assert not os.path.isdir(sub_dir_1)
    assert not os.path.isdir(sub_dir_2)

    pass


def test_make_executable():
    if is_osx:
        path = appdirs.get_temp_dir()
        exe_path = temp_utils.make_temporary_file("test", suffix=".exe", dir=path)

        fs_util.make_executable(None)
        fs_util.make_executable("does_not_exist")
        fs_util.make_executable(exe_path)
        pass

    else:
        fs_util.make_executable(None)


def test_remove_read_only_files_recursive():
    temp_dir = appdirs.get_temp_dir()
    sub_dir_1 = os.path.join(temp_dir, temp_utils.make_random_name(5))
    sub_dir_2 = os.path.join(temp_dir, temp_utils.make_random_name(5))
    sub_sub_dir = os.path.join(sub_dir_2, temp_utils.make_random_name(3))

    os.makedirs(sub_sub_dir)
    os.makedirs(sub_dir_1)

    f1 = temp_utils.make_temporary_file("test", dir=temp_dir)
    f2 = temp_utils.make_temporary_file("test2", dir=sub_dir_1)
    f3 = temp_utils.make_temporary_file("test3", dir=sub_sub_dir)

    os.chmod(f1, stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)
    os.chmod(f2, stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)
    os.chmod(f3, stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)

    assert os.path.isdir(temp_dir)
    assert os.path.isdir(sub_sub_dir)

    lst = fs_util.remove_read_only_files(temp_dir)

    assert not os.path.isdir(sub_sub_dir)
    assert not os.path.isdir(sub_dir_1)


def test_remove_read_only_files_once():
    temp_dir = appdirs.get_temp_dir()
    sub_dir_1 = os.path.join(temp_dir, temp_utils.make_random_name(5))
    sub_dir_2 = os.path.join(temp_dir, temp_utils.make_random_name(5))
    sub_sub_dir = os.path.join(sub_dir_2, temp_utils.make_random_name(3))

    os.makedirs(sub_sub_dir)
    os.makedirs(sub_dir_1)

    f1 = temp_utils.make_temporary_file("test", dir=temp_dir)
    f2 = temp_utils.make_temporary_file("test2", dir=sub_dir_1)
    f3 = temp_utils.make_temporary_file("test3", dir=sub_sub_dir)

    os.chmod(f1, stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)
    os.chmod(f2, stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)
    os.chmod(f3, stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)

    assert os.path.isdir(temp_dir)
    assert os.path.isdir(sub_sub_dir)

    lst = fs_util.remove_read_only_files(temp_dir, recursive=False)

    assert os.path.isdir(sub_sub_dir)
    assert os.path.isdir(sub_dir_1)


def test_get_list_of_files_and_folders_in_tree():
    assert [] == fs_util.get_list_of_files_and_folders_in_tree(None)
    assert [] == fs_util.get_list_of_files_and_folders_in_tree("gibberish")

    temp_dir = appdirs.get_temp_dir()
    sub_dir_1 = os.path.join(temp_dir, temp_utils.make_random_name(5))
    sub_dir_2 = os.path.join(temp_dir, temp_utils.make_random_name(5))
    sub_sub_dir = os.path.join(sub_dir_2, temp_utils.make_random_name(3))

    os.makedirs(sub_sub_dir)
    os.makedirs(sub_dir_1)

    f1 = temp_utils.make_temporary_file("test", dir=temp_dir)
    f2 = temp_utils.make_temporary_file("test2", dir=sub_dir_1)
    f3 = temp_utils.make_temporary_file("test3", dir=sub_sub_dir)

    lst = fs_util.get_list_of_files_and_folders_in_tree(temp_dir)

    assert f1 in lst
    assert f2 in lst
    assert f3 in lst
    assert sub_sub_dir in lst
    assert sub_dir_1 in lst


def test_check_file_open_function():

    path = __file__
    # This file is not open, so should return false
    assert not fs_util.is_file_open_by_another_application( path )

    assert not fs_util.is_file_open_by_another_application( None )

    bad_path = path + "_bad"
    assert not fs_util.is_file_open_by_another_application(bad_path)


def test_replace_folder_dest_does_not_exist():

    temp_dir = appdirs.get_temp_dir()

    dest_dir = tempfile.mkdtemp( prefix="replace_folder_dest_", dir=temp_dir )

    src_dir_parent = tempfile.mkdtemp( prefix="replace_folder_src_", dir=temp_dir )
    src_dir = os.path.join( src_dir_parent, "src" )
    os.makedirs( src_dir + "/src_folder1/src_folder2" )

    fs_util.replace_folder( src_dir, dest_dir )

    dest_dir_backup = os.path.normpath( dest_dir + ".bak" )

    assert not os.path.exists( src_dir )
    assert os.path.exists( dest_dir + "/src_folder1/src_folder2" )

    shutil.rmtree( src_dir_parent )
    shutil.rmtree( dest_dir )

    assert not os.path.exists( dest_dir )
    assert not os.path.exists( src_dir_parent )


@pytest.mark.skipif(not is_osx, reason='OSx implementation for unsupported characters')
def test_serialize_filename_strips_illegal_symbols_positive_osx():
    filename = 'Test file name ([{~`!@#$%^&*()_+|?><\'"}])?.txt'
    serialized_name, modified = fs_util.serialize_filename(filename)
    assert modified is True
    assert serialized_name == 'Test file name ([{~`!@#$%^&*()_+?><\'"}])?.txt'


@pytest.mark.skipif(not is_win, reason='Windows implementation for unsupported characters')
def test_serialize_filename_strips_illegal_symbols_positive_win32():
    filename = 'Test file name ([{~`!@#$%^&*()_+|?><\'"}])?.txt'
    serialized_name, modified = fs_util.serialize_filename(filename)
    assert modified is True
    if sys.platform[:3] == "win":
        assert serialized_name == 'Test file name ([{~`!@#$^&()_+\'}]).txt'
    else:
        assert serialized_name == 'Test file name ([{~`!@#$%^&()_+\'}]).txt'


def test_serialize_filename_strips_dots_positive():
    filename = '.filename.txt.'
    serialized_name, modified = fs_util.serialize_filename(filename)
    assert modified is True
    assert serialized_name == 'filename.txt'


def test_serialize_filename_strips_four_bytes_symbols_positive():
    filename = 'filename with 👀 eyes  👀'
    serialized_name, modified = fs_util.serialize_filename(filename)
    assert modified is True
    assert serialized_name == 'filename with  eyes  '


def test_serialize_filename_does_not_strip_three_bytes_symbols_positive():
    filename = '漢語'
    serialized_name, modified = fs_util.serialize_filename(filename)
    assert modified is False
    assert serialized_name == filename


if __name__ == '__main__':
    pytest.main([__file__, '-s', '-v'])
