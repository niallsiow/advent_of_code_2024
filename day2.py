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
            for i in range(len(report)):
                report_copy = report[:]
                del report_copy[i]
                if is_safe_report(report_copy):
                    safe_reports += 1
                    break
    return safe_reports


input_filename = 'inputs/day2.txt'

reports = []

with open(input_filename) as file:
    for line in file:
        report = line.split(' ')
        for i in range(len(report)):
            report[i] = int(report[i].strip())
        reports.append(report)

print(f'safe reports = {count_safe_reports(reports)}')

print(f'safe reports with dampener = {count_safe_reports_with_dampener(reports)}')
