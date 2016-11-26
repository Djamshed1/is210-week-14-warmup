#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 14 warmup task 02"""

from data import FRUIT

def get_cost_per_item(shoplist):
    """A function that gives cost per item in FRUIT.

    Args:
        shoplist(dict): Is a key item name found in FRUIT and it indicates the number of units
        to purchase.
                        
    Returns:
        A dictionary keyed by the name of fruits with total cost per_item.

    Examples:
        >>> get_cost_per_item({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
        {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
    """
    return {key: FRUIT[key] * shoplist[key] for key in shoplist.iterkeys()
            if key in FRUIT}

def get_total_cost(shoplist):
    """A function to get the total cost.

    Args:
        shoplist(dict): Is a key is the item name found in FRUIT and it indicates
        the number of units to purchase.

    Returns:
        A number indicating the total cost.

    Examples:
        >>> get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
        112.80000000000001
    """
    new_list = get_cost_per_item(shoplist)
    return sum([val for val in new_list.itervalues()])
