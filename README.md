<div align="center">
  <h1><img src="https://emojicdn.elk.sh/🎲" width="30px"> Game of Chance Simulator <img src="https://emojicdn.elk.sh/🎲" width="30px"></h1>
  <p>Explore the world of probability with this interactive casino game simulator!</p>
</div>

## 🚀 Quick Start

1. **Clone the repository:**
   ```sh
   git clone https://github.com/SteveProkovas/Game-of-Chance-Simulator.git
   ```

2. **Navigate to the project directory:**
   ```sh
   cd Game-of-Chance-Simulator
   ```

## 📊 Educational Purpose

This program is designed to be educational, allowing users to experiment with different parameters and understand the concept of probability in casino games. It provides a hands-on way to explore probability theory and its application in real-world scenarios.

## Dice Rolling

While the simulator predominantly focuses on probability distributions for simplicity, we can extend its capabilities to incorporate continuous distributions. By leveraging NumPy's capabilities, we can generate random samples from a normal distribution and analyze their statistical properties.

```python
# Generate random samples from a normal distribution
samples = np.random.normal(mean, std_deviation, num_samples)
```

Here, `mean` and `std_deviation` represent the mean and standard deviation of the distribution, while `num_samples` denotes the number of samples to generate. We can then analyze these samples using advanced statistical techniques, unlocking deeper insights into the underlying probability distribution.

```python
# Analyze the samples using advanced statistical techniques
mean_sample = np.mean(samples)
std_deviation_sample = np.std(samples)
```

The `np.mean()` and `np.std()` functions compute the mean and standard deviation of the generated samples, respectively. These statistics provide valuable insights into the properties of the normal distribution and its relevance to the simulated scenario.

## Coin Flipping

We define four events as follows:

Θ1 = {0 Tails}

Θ2 = {1 Tails}

Θ3 = {2 Tails}

Θ4 = {3 Tails}

## Probabilities
The probabilities for these events are:

Apologies for the confusion. Let's correct that:

| 𝜔𝑖 (Outcome)           | X(𝜔𝑖) (Value) | P(Θ𝑖) (Probability) |
|-----------------------|--------------|-------------------|
| HeadsHeadsHeads (𝜔1) | 0            | 1/8               |
| HeadsHeadsTails (𝜔2) | 1            | 1/8               |
| HeadsTailsHeads (𝜔3) | 1            | 1/8               |
| TailsHeadsHeads (𝜔4) | 1            | 1/8               |
| HeadsTailsTails (𝜔5) | 2            | 1/8               |
| TailsTailsHeads (𝜔6) | 2            | 1/8               |
| TailsHeadsTails (𝜔7) | 2            | 1/8               |
| TailsTailsTails (𝜔8) | 3            | 1/8               |


- P(Θ1) = 1/8
- P(Θ2) = P(Θ3) = 3/8
- P(Θ4) = 1/8

The sum of probabilities is: ∑𝑖=1^4 P(Θ𝑖) = 1

## Card Game : Rummy

1. **Probability of Drawing Specific Cards**:

   ```
   P(C) = (Number of desired cards in the deck) / (Total number of cards remaining in the deck)
   ```

   This equation calculates the probability of drawing a specific card from the deck. You divide the number of desired cards (i.e., cards that would benefit the player) by the total number of cards remaining in the deck.

2. **Probability of Completing Melds**:

   ```
   P(M) = (Number of remaining cards needed to complete meld) / (Total number of cards remaining in the deck)
   ```

   This equation calculates the probability of completing a specific meld, such as a set or a run. You divide the number of remaining cards needed to complete the meld by the total number of cards remaining in the deck.

3. **Optimal Strategy Based on Probabilities**:

   - **Expected Value (EV)**: Calculate the expected value of different actions (e.g., drawing a card, discarding a card) based on their potential outcomes and the probabilities of those outcomes. Choose the action with the highest expected value.

   - **Minimax Algorithm**: Determine the best move that maximizes your chances of winning while minimizing the opponent's chances in a competitive setting.

   - **Monte Carlo Simulation**: Simulate multiple future game states based on different possible actions and their associated probabilities. Evaluate the outcomes of these simulations to inform decision-making.


## 🌟 Feedback and Contributions

Feedback, suggestions, and contributions are always welcome! If you have any ideas to improve the program, feel free to [open an issue](https://github.com/SteveProkovas/Game-of-Chance-Simulator/issues) or [submit a pull request](https://github.com/SteveProkovas/Game-of-Chance-Simulator/pulls).

## 📝 License

This project is licensed under the [Apache License 2.0](LICENSE).

Certainly! Let's integrate the advanced mathematical explanation into the README for the Game of Chance Simulator:
