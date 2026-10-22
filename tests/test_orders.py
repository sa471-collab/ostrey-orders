from ostrey.orders import (Order, apply_discounts, dedupe_orders, order_totals,
                           parse_orders, top_customers)

A = Order("O1", "C1", "R00", 100.0, "")
B = Order("O2", "C2", "R10", 50.0, "SPRING10")
C = Order("O1", "C9", "R05", 999.0, "")


def test_parse():
    assert parse_orders(["O1,C1,R00,100.0,"]) == [A]


def test_dedupe_keeps_first_in_order():
    assert dedupe_orders([A, B, C]) == [A, B]


def test_totals():
    assert order_totals([A, B]) == [105.0, 53.0]


def test_discounts():
    assert apply_discounts([A, B]) == [100.0, 45.0]


def test_top_customers():
    assert top_customers([A, B], 1) == [("C1", 100.0)]
