# /// script
# dependencies = [
# ]
# ///

def calculate_list_distance(left_list, right_list):
    """
    Calculate the total distance between two lists of location IDs.

    Args:
    left_list (list): The first list of location IDs
    right_list (list): The second list of location IDs

    Returns:
    int: Total distance between the sorted lists
    """
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    # Ensure lists are the same length by padding with a large number if needed
    max_length = max(len(left_sorted), len(right_sorted))
    left_sorted += [max(left_sorted + right_sorted)] * (max_length - len(left_sorted))
    right_sorted += [max(left_sorted + right_sorted)] * (max_length - len(right_sorted))

    # Calculate the absolute differences
    distances = [abs(left - right) for left, right in zip(left_sorted, right_sorted)]

    # Return the total distance
    return sum(distances)

# Example input from the problem description
example_left = [3, 4, 2, 1, 3, 3]
example_right = [4, 3, 5, 3, 9, 3]

print("Example Input Distance:", calculate_list_distance(example_left, example_right))

# Function to read input from a file
def read_location_lists(filename):
    """
    Read location lists from a file.

    Args:
    filename (str): Path to the input file

    Returns:
    tuple: Two lists of location IDs
    """
    left_list = []
    right_list = []

    with open(filename, 'r') as file:
        for line in file:
            left, right = map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)

    return left_list, right_list

# Uncomment and use this when you have your input file
input_left, input_right = read_location_lists('./data/day1/input.txt')
print("Puzzle Input Distance:", calculate_list_distance(input_left, input_right))
