import numpy as np

class MinMaxScaler:
    def __init__(self):
        self.minimum = np.array([])
        self.maximum = np.array([])
    def fit(self, data):
        for i in data.T:
            self.minimum = np.append(self.minimum, np.min(i))
            self.maximum = np.append(self.maximum, np.max(i))
        """Store calculated statistics

        Parameters:
        data (np.array): train set, size (num_obj, num_features)
        """
        pass
        
    def transform(self, data):
        data = data.T
        for i in range(data.shape[0]):
            data[i] = (data[i] - self.minimum[i]) / \
                (self.maximum[i] - self.minimum[i])
        # print((data - self.minimum) / (self.maximum - self.minimum))
        return data.T
        """
        Parameters:
        data (np.array): train set, size (num_obj, num_features)

        Return:
        np.array: scaled data, size (num_obj, num_features)
        """
        pass


class StandardScaler:
    def __init__(self):   
        self.mean = np.array([])
        self.sd = np.array([])
    def fit(self, data):
        for i in data.T:
            self.mean = np.append(self.mean, np.mean(i))
            self.sd = np.append(self.sd, np.std(i))
        """Store calculated statistics
        
        Parameters:
        data (np.array): train set, size (num_obj, num_features)
        """
        pass
        
    def transform(self, data):
        data = data.T
        for i in range(data.shape[0]):
            data[i] = (data[i] - self.mean[i]) / self.sd[i]
        return data.T
        """
        Parameters:
        data (np.array): train set, size (num_obj, num_features)

        Return:
        np.array: scaled data, size (num_obj, num_features)
        """
        pass
