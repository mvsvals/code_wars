def series_sum(n):
   return f'{sum([1 / (1 + term * 3) for term in range(0, n)]):.2f}'

print(series_sum(2))