#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
          Copyright Blaze 2021.
 Distributed under the Boost Software License, Version 1.0.
    (See accompanying file LICENSE_1_0.txt or copy at
          https://www.boost.org/LICENSE_1_0.txt)
"""

from typing import List, TypeVar, Dict

from .utils import rand_with_crypto

T = TypeVar('T')


def systematic_sample(population: List[T], n: int, till: int) -> List[T]:
    """
    Systematic (random) sample: 
        A starting point is selected at random, and every `n`th member 
        is selected to be in the sample.

    Args:
        population (List[T]): The list to root the sample from
        n (int): Pick a new member every `n`th member
        till (int): How big (len) should the sample array be

    Returns:
        List[T]: The sample array
    """

    sample: List[T] = []

    # NOTE: randrange doesn't include the LAST NUMBER; randint does.
    x = rand_with_crypto(len(population))

    # Could be more efficient, but this is just for readability.
    while True:
        for i in range(0, len(population), n):
            i += x

            # If i is over length of population, carry on from the beginning.
            if i > len(population) - 1:
                i -= len(population)

                # Don't want i to be negative.
                assert i >= 0

            if len(sample) < till:
                num = population[i]
                sample.append(num)
            else:
                assert len(sample) == till
                return sample


def simple_random_sample(population: List[T], till: int) -> List[T]:
    """
    Simple random sample:
        Every member and set of members has an equal chance of 
        being included in the sample.

    Args:
        population (List[T]): The list to root the sample from
        till (int): How big (len) should the sample array be

    Returns:
        List[T]: The sample array
    """
    sample: List[T] = []

    for _ in range(till):
        # Take a random index from `population`
        sample.append(population[rand_with_crypto(len(population))])

    assert len(sample) == till
    return sample


def stratified_sample(g1: List[T], g2: List[T], till: int) -> List[T]:
    """
    Stratified (random) sample:
        The population is split into two groups (`g1`, `g2`).
        The overall sample consists of some members from every group, 
        and the members from each group are chosen randomly.

    Args:
        g1 (List[T]): First group of the population.
        g2 (List[T]): Second group of the population.
        till (int):  How big (len) should the sample array be

    Returns:
        List[T]: The sample array
    """
    sample: List[T] = []

    total = len(g1) + len(g2)

    # Work out amount of members per group.
    # TODO: this may lead to till_g1 + till_g2 != till
    till_g1 = round(till * len(g1) / total)
    till_g2 = round(till * len(g2) / total)
    assert (till_g1 + till_g2) == till

    sample += simple_random_sample(g1, till_g1)
    sample += simple_random_sample(g2, till_g2)

    assert len(sample) == till
    return sample


def stratified_sample_many(*groups: List[T], till: int) -> List[T]:
    """
    Stratified (random) sample with many groups, the exact same concept as
    `stratified_sample(g1: List[T], g2: List[T], till: int) -> List[T]`


    Args:
        *groups (List[T]): List of groups of the population.
        till (int): How big (len) should the sample array be, 
            note this MUST be a keyword arg else it will be part of `*groups`.

    Returns:
        List[T]: The sample array
    """
    tills: Dict[int, int] = {}
    sample: List[T] = []
    total: int = 0

    for group in groups:
        total += len(group)

    # Iterate over `groups` again.
    for i, group in enumerate(groups):
        tills[i] = round(till * len(group) / total)

    assert sum(tills.values()) == till

    # And again...!
    for i, group in enumerate(groups):
        sample += simple_random_sample(group, tills[i])

    assert len(sample) == till
    return sample
