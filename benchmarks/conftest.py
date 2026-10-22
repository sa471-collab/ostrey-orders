import random

import pytest

from ostrey.orders import Order, TAX_TABLE


@pytest.fixture(scope="session")
def orders():
    rng = random.Random(7)
    regions = [r for r, _ in TAX_TABLE]
    codes = ["", "", "", "SPRING10", "LOYAL15", "STAFF20"]
    base = [
        Order(f"O{i:05d}", f"C{rng.randrange(400):03d}", rng.choice(regions),
              round(rng.uniform(5, 250), 2), rng.choice(codes))
        for i in range(3000)
    ]
    repeats = [base[rng.randrange(len(base))] for _ in range(600)]
    return base + repeats


@pytest.fixture(scope="session")
def order_lines(orders):
    return [f"{o.order_id},{o.customer},{o.region},{o.amount},{o.discount_code}" for o in orders]
