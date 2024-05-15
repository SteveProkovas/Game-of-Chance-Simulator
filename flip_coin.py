import random

def flip_coin(num_flips, bias=None):
  """Flips a biased coin num_flips times and returns a dictionary with heads and tails count.

  Args:
      num_flips: Number of times to flip the coin.
      bias (float, optional): Probability of getting heads. Defaults to 0.5 (fair coin).

  Returns:
      dict: A dictionary containing 'heads' and 'tails' count.
  """
  if bias is None:
    heads_probability = 0.5
  else:
    heads_probability = min(1, max(0, bias))  # Ensure bias is between 0 and 1

  # Early termination for extremely skewed biases (probability close to 0 or 1)
  if heads_probability < 0.01:
    return {'heads': 0, 'tails': num_flips}
  elif heads_probability > 0.99:
    return {'heads': num_flips, 'tails': 0}

  # Use a single counter based on bias
  heads_count = 0
  for _ in range(num_flips):
    if random.random() < heads_probability:
      heads_count += 1
  return {'heads': heads_count, 'tails': num_flips - heads_count}

# Example usage
num_flips = 1000
biased_heads_probability = 0.7  # 70% chance of landing heads
result = flip_coin(num_flips, bias=biased_heads_probability)
print(f"After flipping the biased coin {num_flips} times, we got {result['heads']} heads and {result['tails']} tails.")
