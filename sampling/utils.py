#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
          Copyright Blaze 2021.
 Distributed under the Boost Software License, Version 1.0.
    (See accompanying file LICENSE_1_0.txt or copy at
          https://www.boost.org/LICENSE_1_0.txt)
"""

import logging
import random

__crypto = False


def enable_crypto() -> None:
    global __crypto

    logging.debug('Enabled the use of SystemRandom()')
    __crypto = True


def disable_crypto() -> None:
    global __crypto

    logging.debug('Disabled the use of SystemRandom()')
    __crypto = False


def rand_with_crypto(start: int) -> int:
    if __crypto:
        logging.debug('Using SystemRandom()')
        return random.SystemRandom().randrange(start)
    else:
        return random.randrange(start)
