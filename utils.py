import csv


MONTH_DATE_MAP = {
    '1': 31,
    '2': 28,
    '3': 31,
    '4': 30,
    '5': 31,
    '6': 30,
    '7': 31,
    '8': 31,
    '9': 30,
    '10': 31,
    '11': 30,
    '12': 31,
}


def read_csv(file_name):
    with open(file_name) as file:
        reader = csv.DictReader(file)
        return list(map(convert, reader))


def convert(item):
    result = dict()
    for key, value in item.items():
        result[key] = float(value)
    return result


def get_month_data(data, start_month, end_month):
    start_index = sum([value for key, value in MONTH_DATE_MAP.items() if int(key) < start_month]) * 1_440
    end_index = sum([value for key, value in MONTH_DATE_MAP.items() if int(key) <= end_month]) * 1_440
    return data[start_index:end_index]


def calculate_average_power(data, time=None):
    result = [[]]
    if not time or time == 'minute':
        return sum([data[i]['St'] - data[i - 1]['St'] for i in range(1, len(data))]) / len(data - 1)
    elif time == 'hour':
        period = 60
    elif time == 'day':
        period = 1_440
    elif time == 'week':
        period = 10_107
    elif time == 'month':
        period = 43_800
    elif time == 'season':
        period = 131_400
    elif time == 'year':
        period = 525_600
    for i in range(1, len(data)):
        if i % period == 0:
            result.append([])
        result[-1].append(data[i])
    return [sum(row) for row in result]
