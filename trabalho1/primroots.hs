def primroots(p):
      g = primitive_root(p)
      znorder = p - 1
      is_coprime = lambda x: gcd(x, znorder) == 1
      good_odd_integers = filter(is_coprime, [1..p-1, step=2])
      all_primroots = [power_mod(g, k, p) for k in good_odd_integers]
      all_primroots.sort()
      return all_primroots
