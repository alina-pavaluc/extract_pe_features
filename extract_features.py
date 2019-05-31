import pefile
from magic import magic, os

from extract_and_write_features_to_file import get_debug_size, get_image_version, get_iat_rva, get_export_size, get_check_sum, \
    get_size_of_stack_reserve, get_number_of_sections, get_virtual_size_2, get_resource_size, get_dll_characteristics, \
    get_size_of_initialized_data


def extract_features_from_file(file_name):
    try:
        file_type = magic.from_file(file_name, mime=True)
        if file_type == "application/x-dosexec":
            pe = pefile.PE(file_name, fast_load=True)
            return [get_debug_size(pe), get_image_version(pe), get_iat_rva(pe), get_export_size(pe),
                    get_resource_size(pe), get_virtual_size_2(pe), get_number_of_sections(pe), get_check_sum(pe),
                    get_dll_characteristics(pe), get_size_of_initialized_data(pe), get_size_of_stack_reserve(pe)]
        else:
            return ''
    except Exception as e:
        print(e)


def extract_features_from_folder(folder_name):
    features = []
    for path, subdirs, files in os.walk(folder_name):
        for name in files:
            file_name = os.path.join(path, name)
            try:
                file_type = magic.from_file(file_name, mime=True)
                if file_type == "application/x-dosexec":
                    pe = pefile.PE(file_name, fast_load=True)
                    features.append(
                        [file_name, [get_debug_size(pe), get_image_version(pe), get_iat_rva(pe), get_export_size(pe),
                                     get_resource_size(pe), get_virtual_size_2(pe), get_number_of_sections(pe),
                                     get_check_sum(pe),
                                     get_dll_characteristics(pe), get_size_of_initialized_data(pe),
                                     get_size_of_stack_reserve(pe)]])
            except Exception as e:
                print(e)

    return features
