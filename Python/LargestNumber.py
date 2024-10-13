def find_largest_element(lst):
    """Return the largest element in the list."""
    if not lst:  # Check if the list is empty
        return None  # or raise an exception if preferred

    largest = lst[0]  # Assume the first element is the largest
    for num in lst[1:]:  # Iterate through the rest of the list
        if num > largest:  # If current number is larger
            largest = num  # Update the largest variable

    return largest