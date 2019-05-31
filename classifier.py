import csv
import pickle

import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

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


def train_using_mlp():
    features = []
    labels = []
    with open('C:\\Users\\Alina\\PycharmProjects\\licenta2\\all_features.csv') as feature_file:
        features_files = csv.reader(feature_file, delimiter=',')
        for row in features_files:
            features.append(list(map(float, row[1:-1])))
            labels.append(row[-1])
    y = pd.factorize(labels)[0]
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(100, 50), random_state=1, max_iter= 200)
    clf.fit(features, y)
    filename = 'C:\\Users\\Alina\\PycharmProjects\\licenta2\\MLP_model.sav'
    pickle.dump(clf, open(filename, 'wb'))


def train_using_random_forest_classifier():
    features = []
    labels = []

    feature_names = ['DebugSize', 'ImageVersion','ResourceSize', 'VirtualSize2','CheckSum', 'DLLCharacteristics',
                     'SizeOfInitializedData', 'SizeOfStackReserve']
    with open('C:\\Users\\Alina\\PycharmProjects\\licenta2\\all_features.csv') as feature_file:
        features_files = csv.reader(feature_file, delimiter=',')
        for row in features_files:
            features.append(list(map(float, [row[1], row[2], row[5], row[6], row[8], row[9], row[10], row[11]])))
            labels.append(row[-1])

    y = pd.factorize(labels)[0]

    # X_train, X_test, y_train, y_test = train_test_split(features, y, test_size=0.3)

    clf = RandomForestClassifier(n_jobs=2, random_state=0, n_estimators=100)

    clf.fit(features, y)

    # print(pd.Series(clf.feature_importances_, index=feature_names))

    # clf.fit(X_train, y_train)
    # y_pred = clf.predict(X_test)
    # print("Accuracy:", metrics.accuracy_score(y_test, y_pred))


    # print(clf.predict([[0, 0.0, 278572, 0, 61484, 65536, 3, 46976398, 0, 65536, 1048576]]))
    # print(clf.predict_proba([[0, 0.0, 278572, 0, 61484, 65536, 3, 46976398, 0, 65536, 1048576]]))
    filename = 'C:\\Users\\Alina\\PycharmProjects\\licenta2\\finalized_model_random_forest.sav'
    pickle.dump(clf, open(filename, 'wb'))


def use_classifier():
    filename = 'C:\\Users\\Alina\\PycharmProjects\\licenta2\\finalized_model_random_forest.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict([[0, 0.0, 360448, 0, 292, 2176, 5, 0, 0, 301568, 1048576]])
    prob = loaded_model.predict_proba([[0, 0.0, 360448, 0, 292, 2176, 5, 0, 0, 301568, 1048576]])
    print(result, prob)


if __name__ == "__main__":
    train_using_random_forest_classifier()
    # use_classifier()
