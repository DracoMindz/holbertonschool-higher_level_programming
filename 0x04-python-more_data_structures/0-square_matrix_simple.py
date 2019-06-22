#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    newList = []

    for eachList in matrix:
        for eachNumber in eachList:
            newList.append(eachNumber ** 2)
        newMatrix.append(newList)
        newList = []
    return(newMatrix)
