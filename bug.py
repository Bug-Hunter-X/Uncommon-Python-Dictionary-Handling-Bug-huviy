def function_with_uncommon_error(data):
    # Assume data is a list of dictionaries
    result = {}
    for item in data:
        key = item['key']
        value = item['value']
        # Incorrect logic: Overwrites values if keys are duplicate
        result[key] = value
    return result