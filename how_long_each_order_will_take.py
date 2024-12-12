def order(pizzas, salads, appetizers):
    pizza_prep_time = pizzas * 3 / 2
    pizza_bake_time = pizzas // 10 * 10 + 10

    total_pizza_time = pizza_prep_time + pizza_bake_time
    total_secondary_time = salads * 3 + appetizers * 5
    return max(total_pizza_time, total_secondary_time)