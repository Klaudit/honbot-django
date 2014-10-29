def div(x, y):
    try:
        return round(float(x) / float(y), 4)
    except ZeroDivisionError:
        return 0


def divmin(x, y):
    try:
        return round(float(x) / (float(y) / 60), 4)
    except ZeroDivisionError:
        return 0
