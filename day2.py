def is_safe_report(report):
    if report[1] - report[0] > 0:
        # ascending
        for i in range(1, len(report)):
            if report[i] - report[i - 1] <= 0:
                return False
            elif report[i] - report[i - 1] > 3:
                return False
    elif report[1] - report[0] < 0:
        # descending
        for i in range(1, len(report)):
            if report[i] - report[i - 1] >= 0:
                return False
            elif report[i] - report[i - 1] < -3:
                return False
    else:
        return False
    
    return True


def count_safe_reports(reports):
    safe_reports = 0
    for report in reports:
        if is_safe_report(report):
            safe_reports += 1
    return safe_reports


def count_safe_reports_with_dampener(reports):
    safe_reports = 0
    for report in reports:
        if is_safe_report(report):
            safe_reports += 1
        else:
            # check report with dampener
            # call is_safe_report with indexes missing
            # if true can add and continue
            # if false keep checking
            pass
    return safe_reports


input_filename = 'day2_input.txt'

reports = []

with open(input_filename) as file:
    for line in file:
        report = line.split(' ')
        for i in range(len(report)):
            report[i] = int(report[i].strip())
        reports.append(report)

print(f'safe reports = {count_safe_reports(reports)}')
