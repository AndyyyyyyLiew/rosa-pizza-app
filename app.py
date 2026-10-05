import streamlit as st
import numpy as np
from starter import ZONES, TIME_BLOCKS, COSTS, delivery_times


st.title("Rosa's Pizza Delivery Promise")

st.write(
    "Choose a delivery zone, time block, promise range, and cost assumptions "
    "to find the promised delivery time with the highest net profit."
)


def net_profit(zone, time_block, promise, costs):
    times = delivery_times(zone, time_block, promise, seed=1)

    total_orders = len(times)
    late_orders = np.sum(times > promise)

    cost_per_late_order = (
        costs["refund"]
        + costs["churn_orders"] * costs["margin"]
    )

    total_order_profit = total_orders * costs["margin"]
    total_late_cost = late_orders * cost_per_late_order

    net = total_order_profit - total_late_cost

    return net


def best_promise(zone, time_block, promises, costs):
    best_time = None
    best_profit = -float("inf")

    for promise in promises:
        profit = net_profit(zone, time_block, promise, costs)

        if profit > best_profit:
            best_profit = profit
            best_time = promise

    return best_time, best_profit


zone = st.selectbox(
    "Delivery zone",
    ZONES
)

time_block = st.selectbox(
    "Time block",
    TIME_BLOCKS
)

st.subheader("Promise Range")

min_promise = st.number_input(
    "Minimum promised time (minutes)",
    min_value=5,
    value=5,
    step=5
)

max_promise = st.number_input(
    "Maximum promised time (minutes)",
    min_value=5,
    value=70,
    step=5
)

promise_step = st.number_input(
    "Step size (minutes)",
    min_value=1,
    value=5,
    step=1
)

st.subheader("Cost Assumptions")

refund = st.number_input(
    "Refund cost per late order",
    min_value=0.0,
    value=float(COSTS["refund"]),
    step=1.0
)

churn_orders = st.number_input(
    "Expected future orders lost from one late order",
    min_value=0.0,
    value=float(COSTS["churn_orders"]),
    step=0.1
)

margin = st.number_input(
    "Profit margin per order",
    min_value=0.0,
    value=float(COSTS["margin"]),
    step=1.0
)

user_costs = {
    "refund": refund,
    "churn_orders": churn_orders,
    "margin": margin
}


if st.button("Find Best Promise"):

    if min_promise > max_promise:
        st.error("Minimum promised time must be smaller than maximum promised time.")

    else:
        promises = list(
            range(
                int(min_promise),
                int(max_promise) + 1,
                int(promise_step)
            )
        )

        best_time, best_profit = best_promise(
            zone,
            time_block,
            promises,
            user_costs
        )

        st.success(
            f"Recommended promised delivery time: {best_time} minutes"
        )

        st.write(
            f"Estimated net profit: {best_profit:.2f}"
        )
