# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For
# example, alison heck should be capitalised correctly as Alison Heck.
# Given a full name, your task is to capitalize the name appropriately.

import os


def solve(str):
    return ' '.join(map(str.capitalize, str.split(' ')))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
