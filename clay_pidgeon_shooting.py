def shoot(results):
    pete_shots = ''.join(result[0]['P1'] * (1 + result[1]) for result in results)
    phil_shots = ''.join(result[0]['P2'] * (1 + result[1])  for result in results)
    if pete_shots.count('X') > phil_shots.count('X'):
        return "Pete Wins!"
    elif pete_shots.count('X') < phil_shots.count('X'):
        return 'Phil Wins!'
    return "Draw!"
