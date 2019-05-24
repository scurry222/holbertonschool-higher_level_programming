#!/usr/bin/python3

import numpy


def lazy_matrix_mul(m_a, m_b):
    rows = []
    a_col = 0
    b_row = 0
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a lists of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a lists of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("m_b should contain only integers or floats")
    for row in m_a:
        rows.append(len(row))
    for element in rows:
        if (element != rows[0]):
            raise TypeError("each row of m_a must should be of the same size")
    for row in m_b:
        rows.append(len(row))
    for element in rows:
        if (element != rows[0]):
            raise TypeError("each row of m_b must should be of the same size")

    for col in m_a[0]:
        a_col += 1
    for row in m_b:
        b_row += 1

    if a_col != b_row:
        raise ValueError("m_a and m_b can't be multiplied")

    prod = [[]]
    prod = numpy.matmul(m_a, m_b)

    return prod
