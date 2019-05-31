import csv
import os

import magic
import pefile


def get_all_executable_from_directory(root):
    for path, subdirs, files in os.walk(root):
        for name in files:
            file_name = os.path.join(path, name)
            file_type = magic.from_file(file_name, mime=True)
            if file_type == "application/x-dosexec":
                print(file_name, file_type)


def get_imported_functions(file_path):
    pe = pefile.PE(file_path)
    # for entry in pe.DIRECTORY_ENTRY_IMPORT:
    #     print(entry.dll)
    #     for imp in entry.imports:
    #         print('\t', hex(imp.address), imp.name)

    if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            print("%s" % entry.dll)
            for imp in entry.imports:
                if imp.name is not None:
                    print("\t%s" % imp.name)
                else:
                    print("\tord(%s)" % (str(imp.ordinal)))
            print("\n")


def get_exported_functions(file_path):
    pe = pefile.PE(file_path)
    if hasattr(pe, 'DIRECTORY_ENTRY_EXPORT'):
        for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
            print(exp.name)
    else:
        print('dsfa')


def get_name_of_the_sections(pe):
    sections = []
    for section in pe.sections:
        sections.append(section.Name)
    return sections


def get_dll_characteristics(pe):
    return pe.OPTIONAL_HEADER.DllCharacteristics


def get_export_count(pe):
    return pe.DIRECTORY_ENTRY_EXPORT.struct.NumberOfFunctions


def get_check_sum(pe):
    return pe.OPTIONAL_HEADER.CheckSum


def get_size_of_initialized_data(pe):
    return pe.OPTIONAL_HEADER.SizeOfInitializedData


def get_size_of_stack_reserve(pe):
    return pe.OPTIONAL_HEADER.SizeOfStackReserve


def get_debug_size(pe):
    return pe.OPTIONAL_HEADER.DATA_DIRECTORY[6].Size


def get_image_version(pe):
    return "{}.{}".format(pe.OPTIONAL_HEADER.MajorImageVersion, pe.OPTIONAL_HEADER.MinorImageVersion)


def get_iat_rva(pe):
    return pe.OPTIONAL_HEADER.DATA_DIRECTORY[1].VirtualAddress


def get_export_size(pe):
    return pe.OPTIONAL_HEADER.DATA_DIRECTORY[0].Size


def get_resource_size(pe):
    return pe.OPTIONAL_HEADER.DATA_DIRECTORY[2].Size


def get_virtual_size_2(pe):
    if len(pe.sections) >= 2:
        return pe.sections[1].Misc_VirtualSize


def get_number_of_sections(pe):
    return pe.FILE_HEADER.NumberOfSections


# pe = pefile.PE("E://Sublime Text 3\\msvcr100.dll")
# pe = pefile.PE("C://Users//Alina//Downloads\\Sublime Text Build 3176 x64 Setup.exe")
# print(pe.dump_info())
# print(get_iat_rva(pe))
# print(pe.OPTIONAL_HEADER.SectionAlignment)

# print(get_check_sum(pe))
# print(get_dll_characteristics(pe))
# print(get_size_of_initialized_data(pe))

if __name__ == "__main__":
    with open('features_clean.csv', mode='w', newline='') as feature_file:
        feature_writer = csv.writer(feature_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        feature_writer.writerow(['FilePath', 'DebugSize', 'ImageVersion', 'IatRVA', 'ExportSize',
                                 'ResourceSize', 'VirtualSize2', 'NumberOfSections', 'CheckSum', 'DLLCharacteristics',
                                 'SizeOfInitializedData', 'SizeOfStackReserve', 'Label'])
        for path, subdirs, files in os.walk("E:/arhiva_clean"):
            for name in files:
                file_name = os.path.join(path, name)
                try:
                    file_type = magic.from_file(file_name, mime=True)
                    if file_type == "application/x-dosexec":
                        pe = pefile.PE(file_name, fast_load=True)
                        feature_writer.writerow(
                            [name, get_debug_size(pe), get_image_version(pe), get_iat_rva(pe), get_export_size(pe),
                             get_resource_size(pe), get_virtual_size_2(pe), get_number_of_sections(pe), get_check_sum(pe),
                             get_dll_characteristics(pe), get_size_of_initialized_data(pe), get_size_of_stack_reserve(pe),
                             'clean'])

                except Exception as e:
                    print(e)
