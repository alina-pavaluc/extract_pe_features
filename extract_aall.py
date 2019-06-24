import csv
import os

import pefile
from magic import magic


class PEFileFeatures():

    def __init__(self):

        self.dense_feature_list = None
        self._dense_features = None

        self.set_dense_features(
            ['Machine', 'NumberOfSections', 'TimeDateStamp', 'PointerToSymbolTable', 'NumberOfSymbols',
             'SizeOfOptionalHeader',
             'Characteristics', 'Signature', 'OptionalMagic', 'MajorLinkerVersion',
             'MinorLinkerVersion', 'SizeOfCode',
             'SizeOfInitializedData', 'SizeOfUninitializedData',
             'AddressOfEntryPoint', 'BaseOfCode',
             'ImageBase', 'SectionAlignment', 'FileAlignment',
             'MajorOperatingSystemVersion', 'MinorOperatingSystemVersion',
             'MajorImageVersion', 'MinorImageVersion',
             'MajorSubsystemVersion', 'MinorSubsystemVersion', 'SizeOfImage', 'SizeOfHeaders',
             'CheckSum', 'Subsystem', 'DllCharacteristics',
             'SizeOfStackReserve', 'SizeOfStackCommit',
             'SizeOfHeapReserve', 'SizeOfHeapCommit',
             'LoaderFlags', 'NumberOfRvaAndSizes', 'ExportSize', 'ResourceSize', 'DebugSize', 'VirtualAddress',
             'VirtualSize', 'VirtualSize2', 'GeneratedCheckSum', 'IATRva'
             ])

    def set_dense_features(self, dense_feature_list):
        self.dense_feature_list = dense_feature_list

    def get_dense_features(self):
        return self._dense_features

    def extract_features_using_pefile(self, pe):

        extracted_features = {}
        feature_not_found_flag = -99

        for feature in self.dense_feature_list:
            extracted_features[feature] = feature_not_found_flag

        extracted_features['Machine'] = pe.FILE_HEADER.Machine
        extracted_features['NumberOfSections'] = pe.FILE_HEADER.NumberOfSections
        extracted_features['TimeDateStamp'] = pe.FILE_HEADER.TimeDateStamp
        extracted_features['PointerToSymbolTable'] = pe.FILE_HEADER.PointerToSymbolTable
        extracted_features['NumberOfSymbols'] = pe.FILE_HEADER.NumberOfSymbols
        extracted_features['SizeOfOptionalHeader'] = pe.FILE_HEADER.SizeOfOptionalHeader
        extracted_features['Characteristics'] = pe.FILE_HEADER.Characteristics

        extracted_features['Signature'] = pe.NT_HEADERS.Signature

        extracted_features['OptionalMagic'] = pe.OPTIONAL_HEADER.Magic
        extracted_features['SizeOfImage'] = pe.OPTIONAL_HEADER.SizeOfImage
        extracted_features['SizeOfCode'] = pe.OPTIONAL_HEADER.SizeOfCode
        extracted_features['SizeOfInitializedData'] = pe.OPTIONAL_HEADER.SizeOfInitializedData
        extracted_features['SizeOfUninitializedData'] = pe.OPTIONAL_HEADER.SizeOfUninitializedData
        extracted_features['MajorLinkerVersion'] = pe.OPTIONAL_HEADER.MajorLinkerVersion
        extracted_features['MinorLinkerVersion'] = pe.OPTIONAL_HEADER.MinorLinkerVersion
        extracted_features['AddressOfEntryPoint'] = pe.OPTIONAL_HEADER.AddressOfEntryPoint
        extracted_features['BaseOfCode'] = pe.OPTIONAL_HEADER.BaseOfCode
        extracted_features['ImageBase'] = pe.OPTIONAL_HEADER.ImageBase
        extracted_features['SectionAlignment'] = pe.OPTIONAL_HEADER.SectionAlignment
        extracted_features['FileAlignment'] = pe.OPTIONAL_HEADER.FileAlignment
        extracted_features['MajorOperatingSystemVersion'] = pe.OPTIONAL_HEADER.MajorOperatingSystemVersion
        extracted_features['MinorOperatingSystemVersion'] = pe.OPTIONAL_HEADER.MinorOperatingSystemVersion
        extracted_features['MajorImageVersion'] = pe.OPTIONAL_HEADER.MajorImageVersion
        extracted_features['MinorImageVersion'] = pe.OPTIONAL_HEADER.MinorImageVersion
        extracted_features['MajorSubsystemVersion'] = pe.OPTIONAL_HEADER.MajorSubsystemVersion
        extracted_features['MinorSubsystemVersion'] = pe.OPTIONAL_HEADER.MinorSubsystemVersion
        extracted_features['CheckSum'] = pe.OPTIONAL_HEADER.CheckSum
        extracted_features['SizeOfHeaders'] = pe.OPTIONAL_HEADER.SizeOfHeaders
        extracted_features['Subsystem'] = pe.OPTIONAL_HEADER.Subsystem
        extracted_features['DllCharacteristics'] = pe.OPTIONAL_HEADER.DllCharacteristics
        extracted_features['SizeOfStackReserve'] = pe.OPTIONAL_HEADER.SizeOfStackReserve
        extracted_features['SizeOfHeapReserve'] = pe.OPTIONAL_HEADER.SizeOfHeapReserve
        extracted_features['SizeOfStackCommit'] = pe.OPTIONAL_HEADER.SizeOfStackCommit
        extracted_features['SizeOfHeapCommit'] = pe.OPTIONAL_HEADER.SizeOfHeapCommit
        extracted_features['LoaderFlags'] = pe.OPTIONAL_HEADER.LoaderFlags
        extracted_features['NumberOfRvaAndSizes'] = pe.OPTIONAL_HEADER.NumberOfRvaAndSizes

        extracted_features['ResourceSize'] = pe.OPTIONAL_HEADER.DATA_DIRECTORY[2].Size
        extracted_features['DebugSize'] = pe.OPTIONAL_HEADER.DATA_DIRECTORY[6].Size
        extracted_features['IATRva'] = pe.OPTIONAL_HEADER.DATA_DIRECTORY[1].VirtualAddress
        extracted_features['ExportSize'] = pe.OPTIONAL_HEADER.DATA_DIRECTORY[0].Size

        try:
            extracted_features['GeneratedCheckSum'] = pe.generate_checksum()
        except ValueError:
            print('pe.generate_check_sum() threw an exception, setting to 0!')
            extracted_features['GeneratedCheckSum'] = 0
        if len(pe.sections) > 0:
            extracted_features['VirtualAddress'] = pe.sections[0].VirtualAddress
            extracted_features['VirtualSize'] = pe.sections[0].Misc_VirtualSize

        extracted_features['totalSizePE'] = len(pe.__data__)

        if len(pe.sections) >= 2:
            extracted_features['VirtualSize2'] = pe.sections[1].Misc_VirtualSize

        for feature in self.dense_feature_list:
            if extracted_features[feature] == feature_not_found_flag:
                extracted_features[feature] = ''
                print('Feature not found! Setting to empty')

        self._dense_features = extracted_features
        return self.get_dense_features()


if __name__ == "__main__":
    my_extractor = PEFileFeatures()

    with open('45featscleantest.csv', mode='w', newline='') as feature_file:
        feature_writer = csv.writer(feature_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        feature_writer.writerow(['fileName', my_extractor.dense_feature_list, 'Label'])
        for path, subdirs, files in os.walk("E:/cleantest"):
            for name in files:
                file_name = os.path.join(path, name)
                try:
                    file_type = magic.from_file(file_name, mime=True)
                    if file_type == "application/x-dosexec":
                        pe = pefile.PE(file_name, fast_load=True)
                        features = my_extractor.extract_features_using_pefile(pe)
                        feature_writer.writerow(
                            [name, *[features.get(key, '') for key in my_extractor.dense_feature_list], 'clean'])

                except Exception as e:
                    print(e)
