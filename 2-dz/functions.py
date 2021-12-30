from typing import List


def prod_non_zero_diag(X: List[List[int]]) -> int:
    result = -1
    for i in range(min(len(X), len(X[0]))):
        if X[i][i]:
            result *= X[i][i]
    if result != -1:
        result *= -1
    return result
    pass


def are_multisets_equal(x: List[int], y: List[int]) -> bool:
    return sorted(x) == sorted(y)
    pass


def max_after_zero(x: List[int]) -> int:
    m = -1
    for i in range(1,len(x)):
        if x[i-1] == 0 and x[i] > m:
            m = x[i]
    return m
    pass


def convert_image(image: List[List[List[float]]], weights: List[float]) -> List[List[float]]:
    # print(len(image), len(image[0]), len(image[0][0]))
    # print(len(weights))
    res_list = []
    for i in range(len(image)):
        zeros = []
        for i in range(len(image[0])):
            zeros.append(0)
        res_list.append(zeros)

    for i in range(len(image)):
        for j in range(len(image[0])):
            for k in range(len(image[0][0])):
                res_list[i][j] += weights[k] * image[i][j][k]
    return res_list
    pass


def run_length_encoding(x: List[int]) -> (List[int], List[int]):
    list_number = []
    list_reps = []
    last_end = 0
    for i in range(1,len(x)):
        if x[i - 1] != x[i]:
            list_number.append(x[i - 1])
            list_reps.append(i - last_end)
            last_end = i
    list_number.append(x[len(x) - 1])
    list_reps.append(len(x) - last_end)
    return (list_number, list_reps)
    pass


def pairwise_distance(X: List[List[float]], Y: List[List[float]]) -> List[List[float]]:
    res = []
    for i in range(len(X)):
        res.append([0] * len(Y))
    for i in range(len(X)):
        for j in range(len(Y)):
            calc = 0
            for k in range(len(X[0])):
                calc += (X[i][k] - Y[j][k]) ** 2
            res[i][j] = (calc) ** (1/2)
    return res
    pass
