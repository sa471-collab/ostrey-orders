from dataclasses import dataclass
import heapq

TAX_TABLE = [(f"R{i:02d}", round(0.05 + i * 0.001, 3)) for i in range(60)]


@dataclass(frozen=True)
class Order:
    order_id: str
    customer: str
    region: str
    amount: float
    discount_code: str = ""


def parse_orders(lines):
    """Parse 'order_id,customer,region,amount,discount_code' lines."""
    orders = []
    for line in lines:
        order_id, customer, region, amount, code = line.strip().split(",")
        orders.append(Order(order_id, customer, region, float(amount), code))
    return orders


def dedupe_orders(orders):
    """Drop repeat order_ids, keeping the first one seen."""
    seen = set()
    unique = []
    for order in orders:
        if order.order_id not in seen:
            seen.add(order.order_id)
            unique.append(order)
    return unique


def order_totals(orders):
    """Amount plus regional tax for each order."""
    totals = []
    for order in orders:
        rates = {region: rate for region, rate in TAX_TABLE}
        totals.append(round(order.amount * (1 + rates[order.region]), 2))
    return totals


DISCOUNTS = {"SPRING10": 0.10, "LOYAL15": 0.15, "STAFF20": 0.20}


def apply_discounts(orders):
    """Amount after any discount code."""
    return [round(o.amount * (1 - DISCOUNTS.get(o.discount_code, 0.0)), 2) for o in orders]


def top_customers(orders, n=10):
    """The n customers with the most spend."""
    spend = {}
    for order in orders:
        spend[order.customer] = spend.get(order.customer, 0.0) + order.amount
    return heapq.nlargest(n, spend.items(), key=lambda kv: kv[1])
