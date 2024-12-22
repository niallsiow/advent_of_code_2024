def page_follows_rules(rules, pages_printed, update, page):
    if page not in rules:
        return True

    for dependant_page in rules[page]:
        if dependant_page in update and dependant_page not in pages_printed:
            return False
    return True 


def is_update_valid(rules, update):
    pages_printed = []
    for page in update:
        if not page_follows_rules(rules, pages_printed, update, page):
            return False
        pages_printed.append(page)
    return True


def sum_middle_pages(rules, updates):
    sum = 0
    for update in updates:
        sum += int(update[len(update) // 2])
    return sum


def sum_valid_middle_pages(rules, updates):
    valid_updates = []
    for update in updates:
        if is_update_valid(rules, update):
            valid_updates.append(update)
    return sum_middle_pages(rules, valid_updates)


def correct_update(rules, update):
    corrected_update = []
    pages_to_order = update[:]
    
    i = 0
    while pages_to_order:
        if page_follows_rules(rules, corrected_update, update, pages_to_order[i]):
            corrected_update.append(pages_to_order[i])
            del pages_to_order[i]
        i += 1
        if i >= len(pages_to_order):
            i = 0
    return corrected_update


def get_corrected_updates(rules, incorrect_updates):
    corrected_updates = []
    for incorrect_update in incorrect_updates:
        corrected_updates.append(correct_update(rules, incorrect_update))
    return corrected_updates
        

def sum_corrected_middle_pages(rules, updates):
    incorrect_updates = []
    for update in updates:
        if not is_update_valid(rules, update):
            incorrect_updates.append(update)
    return sum_middle_pages(rules, get_corrected_updates(rules, incorrect_updates))


def get_input(filename):
    rules = {}
    updates = []
    with open(filename) as file:
        for line in file.readlines():
            if '|' in line:
                dependant_page, page = line.strip().split('|')
                if page in rules:
                    rules[page].append(dependant_page)
                else:
                    rules[page] = [dependant_page]
            elif line.strip() != '':
                updates.append(line.strip().split(','))

    return rules, updates


filename = 'inputs/day5.txt'
rules, updates = get_input(filename)

print(f'sum of valid middle page = {sum_valid_middle_pages(rules, updates)}')

print(f'sum of corrected middle page = {sum_corrected_middle_pages(rules, updates)}')
