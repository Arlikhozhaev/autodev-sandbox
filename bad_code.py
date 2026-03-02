def _process_item(item):
    if isinstance(item, int):
        if item % 2 == 0:
            return item * 2
        return item * 3

    if isinstance(item, str):
        if len(item) > 3:
            return item.upper()
        return item.lower()

    return None


def process_data(data):
    result = []
    for i in range(len(data)):
        result.append(_process_item(data[i]))
    return result

        result.append(_process_item(data[i]))
    return result

        result.append(_process_item(data[i]))
    return result

        result.append(_process_item(data[i]))
    return result

        result.append(_process_item(data[i]))
    return result

