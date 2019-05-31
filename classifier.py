import csv
import pickle

import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

from extract_features import extract_features_from_file, extract_features_from_folder


class Classifier:
    def __init__(self, filename):
        self.loaded_model = pickle.load(open(filename, 'rb'))
        self.target_names = ['clean', 'malware']

    def label_file(self, extracted_features):
        predicted = self.loaded_model.predict([extracted_features])[0]
        return self.target_names[predicted], self.loaded_model.predict_proba([extracted_features])[0][predicted]

    def classify_file(self, filename):
        extracted_features = extract_features_from_file(filename)
        if extracted_features != '':
            return self.label_file(extracted_features)
        else:
            return 'this is not an application, so it\'s not a threat', '1.0'

    def scan_folder(self, folder_name):
        out = []
        try:
            features = extract_features_from_folder(folder_name)
            for file_features in features:
                out.append([file_features[0], self.label_file(file_features[1])])
        except Exception as e:
            print(e)
        return out


def train_using_decision_tree_classifier():
    features = []
    labels = []
    with open('C:\\Users\\Alina\\PycharmProjects\\licenta2\\all_features.csv') as feature_file:
        features_files = csv.reader(feature_file, delimiter=',')
        for row in features_files:
            features.append(row[1:-1])
            labels.append(row[-1])

    # target_names = ['clean', 'malware']
    # features_name = ['DebugSize', 'ImageVersion', 'IatRVA', 'ExportSize',
    #                  'ResourceSize', 'VirtualSize2', 'NumberOfSections', 'CheckSum', 'DLLCharacteristics',
    #                  'SizeOfInitializedData', 'SizeOfStackReserve']
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features, labels)
    filename = 'C:\\Users\\Alina\\PycharmProjects\\licenta2\\finalized_model.sav'
    pickle.dump(clf, open(filename, 'wb'))


def train_using_random_forest_classifier():
    features = []
    labels = []

    with open('C:\\Users\\Alina\\PycharmProjects\\licenta2\\all_features.csv') as feature_file:
        features_files = csv.reader(feature_file, delimiter=',')
        for row in features_files:
            features.append(row[1:-1])
            labels.append(row[-1])

    y = pd.factorize(labels)[0]
    clf = RandomForestClassifier(n_jobs=2, random_state=0)

    clf.fit(features, y)

    # print(clf.predict([[0, 0.0, 278572, 0, 61484, 65536, 3, 46976398, 0, 65536, 1048576]]))
    # print(clf.predict_proba([[0, 0.0, 278572, 0, 61484, 65536, 3, 46976398, 0, 65536, 1048576]]))
    filename = 'C:\\Users\\Alina\\PycharmProjects\\licenta2\\finalized_model_random_forest.sav'
    pickle.dump(clf, open(filename, 'wb'))


def use_classifier():
    filename = 'C:\\Users\\Alina\\PycharmProjects\\licenta2\\finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict([[0, 0.0, 29948, 0, 928, 2618, 4, 0, 0, 28672, 1048576]])
    print(result)



if __name__ == "__main__":
    train_using_random_forest_classifier()
