#!/usr/bin/env python3

from collections.abc import Callable
from typing import Any

products: list[dict[str, Any]] = [
    {"name": "Laptop", "price": 89990, "discount": 10},
    {"name": "Mouse", "price": 2490, "discount": 15},
    {"name": "Keyboard", "price": 5490, "discount": 0},
    {"name": "Monitor", "price": 27990, "discount": 25},
]

dobavit_final_price: Callable[[dict[str, Any]], dict[str, Any]] = lambda tovar: {
    **tovar,
    "final_price": tovar["price"] * (1 - tovar["discount"] / 100),
}

if __name__ == "__main__":
    tovary_s_tsenoy: list[dict[str, Any]] = sorted(
        map(dobavit_final_price, products), key=lambda tovar: tovar["final_price"]
    )
    print(f"Обработано товаров: {len(tovary_s_tsenoy)}")

    for tovar in tovary_s_tsenoy:
        print(tovar)
