import numpy as np
from collections import defaultdict

def kfold_split(num_objects, num_folds):
    result = []
    step = int(num_objects / num_folds)
    current = 0
    for i in range(num_folds):
        r = np.arange(num_objects)
        s = r[current:current+step]
        f = np.concatenate((r[0:current], r[current+step:num_objects]), \
                axis=None)
        if i == num_folds - 1:
            s = r[current:num_objects]
            f = r[0:current]
        result.append((f, s))
        current = current + step
    return result
    pass

def knn_cv_score(X, y, parameters, score_function, folds, knn_class):
    results = dict()
    for normalizer in parameters['normalizers']:
        for i in folds:
            if normalizer[0] is not None:
                scaler = normalizer[0]
                scaler.fit(X[i[0]])
                t_X_0 = scaler.transform(X[i[0]])
                t_X_1 = scaler.transform(X[i[1]])
            else:
                t_X_0 = X[i[0]]
                t_X_1 = X[i[1]]
            for n_n in parameters['n_neighbors']:
                for metric in parameters['metrics']:
                    for weight in parameters['weights']:
                            if (normalizer[1], n_n, metric, weight) \
                                    not in results:
                                results[(normalizer[1], n_n, metric, weight)] = 0
                            neigh = knn_class(n_neighbors = n_n, \
                                              weights = weight, \
                                              metric = metric)
                            neigh.fit(t_X_0, y[i[0]])
                            y_predict = neigh.predict(t_X_1)
                            value = score_function(y[i[1]], y_predict)
                            results[(normalizer[1], n_n, metric, weight)] += \
                                score_function(y[i[1]], y_predict)
    for i in results:
        results[i] /= len(folds)
    return results
