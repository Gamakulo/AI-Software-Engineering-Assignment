# Write a Python function that sorts a list of dictionaries by a specified key
def sort_dicts_by_key(dicts, key):
    """
    Sorts a list of dictionaries by a specified key.

    Parameters:
    dicts (list): A list of dictionaries to be sorted.
    key (str): The key in the dictionaries to sort by.

    Returns:
    list: A new list of dictionaries sorted by the specified key.
    """
    return sorted(dicts, key=lambda x: x[key])

# Manually Written Function
def manual_sort_dicts_by_key(dicts, key):
    """
    Manually sorts a list of dictionaries by a specified key using a simple
    bubble sort algorithm for comparison purposes.
    """
    n = len(dicts)
    for i in range(n):
        for j in range(0, n - i - 1):
            if dicts[j][key] > dicts[j + 1][key]:
                dicts[j], dicts[j + 1] = dicts[j + 1], dicts[j]
    return dicts
# Example usage
if __name__ == "__main__":
    data = [
        {"name": "omo", "age": 25},
        {"name": "Bobo", "age": 20},
        {"name": "Ade", "age": 30}
    ]

    print("AI-Generated:", sort_dicts_by_key(data, "age"))
    print("Manual:", manual_sort_dicts_by_key(data.copy(), "age"))
    data