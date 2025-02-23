def function_with_uncommon_error_fixed(data):
    result = {}
    for item in data:
        key = item['key']
        value = item['value']
        # Correct logic: Aggregates values if keys are duplicate
        if key in result:
            if isinstance(result[key], list):
                result[key].append(value)
            else:
                result[key] = [result[key], value]
        else:
            result[key] = value
    return result