#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sampling import systematic_sample, enable_crypto, simple_random_sample, \
    stratified_sample, stratified_sample_many

arr = [x for x in range(100)]
arr1 = ['a', 'b', 'c']
arr2 = ['x', 'y']

# Or disable_crypto(), crypto is disabled by default.
enable_crypto()
print(systematic_sample(arr, 10, 5))
print(simple_random_sample(arr, 5))
print(stratified_sample(arr, arr1, 5))
print(stratified_sample_many(arr, arr1, arr2, till=5))
