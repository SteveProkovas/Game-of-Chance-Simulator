import random
import matplotlib.pyplot as plt
import numpy as np

def roll_dice(num_dice, num_sides):
    """Simulate rolling multiple dice."""
    return [random.randint(1, num_sides) for _ in range(num_dice)]

def calculate_probabilities(num_dice, num_sides, num_rolls):
    """Calculate the probabilities of each outcome."""
    outcomes = {}
    total_outcomes = num_dice * num_sides

    # Calculate all possible sums
    possible_sums = [i + 1 for i in range(num_dice, num_dice * num_sides)]

    # Initialize outcome counts to 0
    for sum_ in possible_sums:
        outcomes[sum_] = 0

    # Perform the specified number of rolls
    for _ in range(num_rolls):
        # Roll the dice and calculate the sum of the rolls
        roll_sum = sum(roll_dice(num_dice, num_sides))
        # Update the count of occurrences for each sum
        outcomes[roll_sum] += 1

    # Calculate probabilities by dividing the count of occurrences by the total number of rolls
    probabilities = {k: v / num_rolls for k, v in outcomes.items()}
    return probabilities

def visualize_probabilities(probabilities, color='skyblue'):
    """Visualize the probabilities with a histogram."""
    # Create a bar chart to visualize the probabilities
    plt.bar(probabilities.keys(), probabilities.values(), color=color)
    plt.xlabel('Sum of Dice')
    plt.ylabel('Probability')
    plt.title('Probability Distribution of Rolling Dice')
    plt.show()

def calculate_statistics(probabilities):
    """Calculate additional statistics from the probability distribution using numpy."""
    outcomes = np.array(list(probabilities.keys()))
    probabilities_values = np.array(list(probabilities.values()))
    
    # Calculate mean
    mean = np.dot(outcomes, probabilities_values)
    
    # Calculate standard deviation
    variance = np.dot((outcomes - mean) ** 2, probabilities_values)
    std_deviation = np.sqrt(variance)
    
    # Calculate percentiles (25th, 50th, 75th)
    percentiles = np.percentile(outcomes, [25, 50, 75], interpolation='nearest', axis=0, weights=probabilities_values)
    
    return {'mean': mean, 'standard_deviation': std_deviation, 'percentiles': percentiles}

def main():
    """Main function to run the program."""
    # Prompt the user to input the number of dice, number of sides, and number of rolls
    num_dice = int(input("Enter the number of dice: "))
    num_sides = int(input("Enter the number of sides on each die: "))
    num_rolls = int(input("Enter the number of rolls: "))

    # Simulate rolling the dice and calculate probabilities
    print("\nSimulating rolling", num_dice, "dice", num_rolls, "times...")
    probabilities = calculate_probabilities(num_dice, num_sides, num_rolls)

    # Print probabilities of each outcome
    print("\nProbabilities of each outcome:")
    for outcome, probability in sorted(probabilities.items()):
        print("Sum:", outcome, "- Probability:", probability)

    # Visualize the probabilities using a histogram
    visualize_probabilities(probabilities)

    # Calculate additional statistics
    stats = calculate_statistics(probabilities)
    print("\nAdditional statistics:")
    print("Mean:", stats['mean'])
    print("Standard Deviation:", stats['standard_deviation'])
    print("25th Percentile:", stats['percentiles'][0])
    print("50th Percentile (Median):", stats['percentiles'][1])
    print("75th Percentile:", stats['percentiles'][2])

if __name__ == "__main__":
    main()
