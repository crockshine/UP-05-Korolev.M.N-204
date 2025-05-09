def find_index(data, hsh):
    current_index = -1

    for i, track in enumerate(data):
        if track == hsh:
            current_index = i
            break

    return current_index