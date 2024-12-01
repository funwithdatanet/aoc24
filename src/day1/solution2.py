# /// script
# dependencies = [
# ]
# ///

def calculate_similarity_score(left_list, right_list):
    """
    Calculate the similarity score between two lists.

    Args:
    left_list (list): The first list of location IDs
    right_list (list): The second list of location IDs

    Returns:
    int: Similarity score
    """
    # Count occurrences of each number in the right list
    right_counts = {}
    for num in right_list:
        right_counts[num] = right_counts.get(num, 0) + 1

    # Calculate similarity score
    similarity_score = 0
    for left_num in left_list:
        # Get the number of occurrences (default to 0 if not found)
        occurrences = right_counts.get(left_num, 0)

        # Add to similarity score
        similarity_score += left_num * occurrences

    return similarity_score

# Example input from the problem description
example_left = [3, 4, 2, 1, 3, 3]
example_right = [4, 3, 5, 3, 9, 3]

print("Example Similarity Score:",
      calculate_similarity_score(example_left, example_right))

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

input_left, input_right = read_location_lists('./data/day1/input.txt')
print("Puzzle Similarity Score:",
      calculate_similarity_score(input_left, input_right))
