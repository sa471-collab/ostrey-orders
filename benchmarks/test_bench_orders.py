from ostrey.orders import (apply_discounts, dedupe_orders, order_totals,
                           parse_orders, top_customers)


def test_parse_orders(benchmark, order_lines):
    benchmark(parse_orders, order_lines)


def test_dedupe_orders(benchmark, orders):
    benchmark(dedupe_orders, orders)


def test_order_totals(benchmark, orders):
    benchmark(order_totals, orders)


def test_apply_discounts(benchmark, orders):
    benchmark(apply_discounts, orders)


def test_top_customers(benchmark, orders):
    benchmark(top_customers, orders, 10)
