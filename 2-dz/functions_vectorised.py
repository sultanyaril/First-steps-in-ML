import numpy as np


def prod_non_zero_diag(X: np.ndarray) -> int:
    diag = np.diag(X)
    product = np.prod(diag[diag != 0])
    if product == 1:
        return (-1)
    return product
    pass


def are_multisets_equal(x: np.ndarray, y: np.ndarray) -> bool:
    return np.array_equal(np.sort(x), np.sort(y))
    pass


def max_after_zero(x: np.ndarray) -> int:
    print(x)
    return int(np.amax(np.array([x[i + 1] for i in np.where(x == 0) if np.any(i != len(x) - 1)]), initial=-1))
    pass


def convert_image(image: np.ndarray, weights: np.ndarray) -> np.ndarray:
    res = weights[0] * image[:,:,0]
    if (image.shape[1] <= 5):
        print(res)
    for i in range(1,image.shape[2]):
        res += weights[i] * image[:,:,i]
    return res
    """
    Sum up image channels with weights.

    Return type: np.ndarray
    """
    pass


def run_length_encoding(x: np.ndarray) -> (np.ndarray, np.ndarray):
    y = np.array(x[1:] != x[:-1])
    i = np.append(np.where(y), len(x) - 1)
    z = np.diff(np.append(-1, i))
    return(x[i], z)        
    pass


def pairwise_distance(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    return np.linalg.norm(X[:, None, :] - Y[None, :, :], axis=-1)
    pass
