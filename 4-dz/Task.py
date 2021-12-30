import numpy as np


class Preprocesser:
    
    def __init__(self):
        pass
    
    def fit(self, X, Y=None):
        pass
    
    def transform(self, X):
        pass
    
    def fit_transform(self, X, Y=None):
        pass
    
    
class MyOneHotEncoder(Preprocesser):
    
    def __init__(self, dtype=np.float64):
        super(Preprocesser).__init__()
        self.dtype = dtype
        
    def fit(self, X, Y=None):
        self.paras = dict()
        for i in X.columns:
            self.paras[i] = sorted(X[i].unique())
        pass
    
    def transform(self, X):
        row_list = []
        columns = []
        for i in self.paras:
            columns.append(self.paras[i])
        for index, row in X.iterrows():
            l = self.paras
            for i in l:
                l[i] = dict(zip(l[i], [0] * len(l[i])))
            for i in l:
                l[i][row[i]] = 1
            flat_l = []
            for i in l:
                for j in l[i]:
                    flat_l.append(l[i][j])
            row_list.append(flat_l)
        return np.array(row_list)
    
    def fit_transform(self, X, Y=None):
        self.fit(X)
        return self.transform(X)
    
    def get_params(self, deep=True):
        return {"dtype": self.dtype}
    
    
class SimpleCounterEncoder:
    
    def __init__(self, dtype=np.float64):
        self.dtype=dtype
        
    def fit(self, X, Y):
        self.paras = dict()
        for i in X.columns:
            self.paras[i] = dict()
            u = sorted(X[i].unique())
            for j in u:
                indices = np.array([])
                for index, row in X.iterrows():
                    if row[i] == j:
                        indices = np.append(indices, index)
                self.paras[i][j] = []
                f = np.sum(Y[indices]) / len(indices)
                s = len(indices) / X.shape[0]
                self.paras[i][j].append(f)
                self.paras[i][j].append(s)
                self.paras[i][j].append(0)
    def transform(self, X, a=1e-5, b=1e-5):
        row_list = []
        for index, row in X.iterrows():
            l = []
            for name in X.columns:
                value = row[name]
                print(name)
                new = self.paras[name][value]
                new[2] = (new[0] + a) / (new[1] + b)
                l.extend(new)
            row_list.append(l)
        return np.array(row_list)
    
    def fit_transform(self, X, Y, a=1e-5, b=1e-5):
        self.fit(X, Y)
        return self.transform(X, a, b)
    
    def get_params(self, deep=True):
        return {"dtype": self.dtype}

    
def group_k_fold(size, n_splits=3, seed=1):
    idx = np.arange(size)
    np.random.seed(seed)
    idx = np.random.permutation(idx)
    n_ = size // n_splits
    for i in range(n_splits - 1):
        yield idx[i * n_ : (i + 1) * n_], np.hstack((idx[:i * n_], idx[(i + 1) * n_:]))
    yield idx[(n_splits - 1) * n_ :], idx[:(n_splits - 1) * n_]

    
class FoldCounters:
    
    def __init__(self, n_folds=3, dtype=np.float64):
        self.dtype = dtype
        self.n_folds = n_folds
        
    def fit(self, X, Y, seed=1):
        self.folds = []      
        self.fits = []
        for i in group_k_fold(X.shape[0], self.n_folds, seed):
            f = SimpleCounterEncoder()
            f.fit(X.loc[i[1]], Y[i[1]])
            self.fits.append(f)
            self.folds.append(i)
            
    def transform(self, X, a=1e-5, b=1e-5):
        cnt = 0
        res = np.empty((X.shape[0], X.shape[1] * 3))
        for i in self.folds:
            for j in i[0]:
                res[j] = self.fits[cnt].transform(X.loc[j].to_frame().transpose(), a, b)
            cnt += 1
        return res
        
    def fit_transform(self, X, Y, a=1e-5, b=1e-5):
        self.fit(X, Y)
        return self.transform(X, a, b)
 
       
def weights(x, y):
    u = sorted(np.unique(x))
    res = dict(zip(u, [0] * len(u)))
    totals = dict(zip(u, [0] * len(u)))
    for i in range(len(x)):
        if y[i] == 1:
            res[x[i]] += 1
        totals[x[i]] += 1
    res = np.array(list(res.values()))
    totals = np.array(list(totals.values()))
    return res / totals
            
    """
    param x: training set of one feature, numpy-array, shape [n_objects,]
    param y: target for training objects, numpy-array, shape [n_objects,]
    returns: optimal weights, numpy-array, shape [|x unique values|,]
    """
    #your code here
