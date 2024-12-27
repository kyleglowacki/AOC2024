import aocd
from collections import defaultdict, deque

def parseData(rawlines):
    rules = ""
    pages = ""
    for line in rawlines:
        if "|" in line:
            ## rule
            rules += f"\n{line}"
            
        elif "," in line:
            ## pages
            pages += f"\n{line}"

    #print(rules)
    #print(pages)
    return rules, pages

def parse_input(rules, updates):
    rules_list = [tuple(map(int, rule.split('|'))) for rule in rules.strip().split()]
    updates_list = [list(map(int, update.split(','))) for update in updates.strip().split()]
    return rules_list, updates_list

def is_correct_order(update, rules):
    index_map = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:
        if x in index_map and y in index_map:
            if index_map[x] > index_map[y]:
                return False
    return True

def middle_page_number(update):
    return update[len(update) // 2]

def topological_sort(nodes, edges):
    in_degree = {node: 0 for node in nodes}
    adj_list = defaultdict(list)
    
    for x, y in edges:
        adj_list[x].append(y)
        in_degree[y] += 1
    
    queue = deque([node for node in nodes if in_degree[node] == 0])
    sorted_list = []
    
    while queue:
        node = queue.popleft()
        sorted_list.append(node)
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_list

def reorder_update(update, rules):
    nodes = set(update)
    edges = [(x, y) for x, y in rules if x in nodes and y in nodes]
    sorted_update = topological_sort(nodes, edges)
    return sorted_update

raw = aocd.get_data(day=5, year=2024)
data = raw.splitlines()


# Example input
rules = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""

updates = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

rules, updates = parseData(data)
rules_list, updates_list = parse_input(rules, updates)
    
correct_updates = []
incorrect_updates = []
    
for update in updates_list:
    if is_correct_order(update, rules_list):
        correct_updates.append(update)
    else:
        incorrect_updates.append(update)
    
middle_numbers_sum = sum(middle_page_number(update) for update in correct_updates)

print("FIRST STAR")
print(f"first total = {middle_numbers_sum}")

   
reordered_updates = [reorder_update(update, rules_list) for update in incorrect_updates]
middle_numbers_sum_incorrect = sum(middle_page_number(update) for update in reordered_updates)


print("SECOND STAR")
print(f"second total = {middle_numbers_sum_incorrect}")
