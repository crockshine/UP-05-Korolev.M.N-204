def trim_string(string, max_length=16):
    return string[:max_length] + '...' if len(string) > max_length else string