"""
Prints out all the melons in our inventory
"""

from melons import (
    melon_names,
    melon_seedlessness,
    melon_prices,
    melon_flesh_color,
    melon_rind_color,
    melon_avg_weight,
)


def print_melon(name, seedless, price, flesh_color, rind_color, avg_weight):
    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print """{}s {} seeds are ${:.2f}, are {} inside and {} outside, and weigh (on average) {} pounds.""".format(
                                    name,
                                    have_or_have_not,
                                    price, 
                                    flesh_color,
                                    rind_color,
                                    avg_weight,
                                )


for i in melon_names:
    print_melon(
        melon_names[i],
        melon_seedlessness[i],
        melon_prices[i],
        melon_flesh_color[i],
        melon_rind_color[i],
        melon_avg_weight[i],
    )
