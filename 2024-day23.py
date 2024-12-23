import aocd
import copy
import itertools
import math



def convert_string_to_int(ls):
    return list(map(int, ls))

def make_matrix(l, w, v):
    return [[v for _ in range(w)] for _ in range(l)]

def count_matrix_items(m, v):
    cnt=0
    for y, row in enumerate(m):
        for x, col in enumerate(row):
            if col == v:
                cnt += 1
    return cnt

def on_board(farm, x, y):
    if (x < 0) or (y < 0):
        return False
    if (x >= len(farm[0])) or (y >= len(farm)):
        return False
    return True

def find_triplets_optimized(connections):
    from collections import defaultdict

    # Build the adjacency dictionary
    adjacency_dict = defaultdict(set)
    for connection in connections:
        a, b = connection.split('-')
        adjacency_dict[a].add(b)
        adjacency_dict[b].add(a)

    # Find all triplets
    triplets = set()
    for a in adjacency_dict:
        for b in adjacency_dict[a]:
            if b > a:  # Ensure each pair is considered only once
                for c in adjacency_dict[a]:
                    if c > a and c in adjacency_dict[b]:
                        triplet = tuple(sorted([a, b, c]))
                        triplets.add(triplet)

    return triplets

def filter_triplets(triplets):
    filtered_triplets = [triplet for triplet in triplets if any(computer.startswith('t') for computer in triplet)]
    return filtered_triplets


raw = aocd.get_data(day=23, year=2024)

data = raw.splitlines()

# Find all triplets
all_triplets = find_triplets_optimized(data)

# Filter triplets containing at least one computer starting with 't'
filtered_triplets = filter_triplets(all_triplets)

# Count filtered triplets
count_filtered_triplets = len(filtered_triplets)
print("Count of filtered triplets:", count_filtered_triplets)


print("FIRST STAR")
print(f"first total = {count_filtered_triplets}")

from collections import defaultdict

def build_adjacency_dict(connections):
    adjacency_dict = defaultdict(set)
    for connection in connections:
        a, b = connection.split('-')
        adjacency_dict[a].add(b)
        adjacency_dict[b].add(a)
    return adjacency_dict

def bron_kerbosch(R, P, X, adjacency_dict, cliques):
    if not P and not X:
        cliques.append(R)
        return
    for v in list(P):
        bron_kerbosch(R.union([v]), P.intersection(adjacency_dict[v]), X.intersection(adjacency_dict[v]), adjacency_dict, cliques)
        P.remove(v)
        X.add(v)

def find_maximal_cliques(adjacency_dict):
    P = set(adjacency_dict.keys())
    R = set()
    X = set()
    cliques = []
    bron_kerbosch(R, P, X, adjacency_dict, cliques)
    return cliques

def find_largest_clique(cliques):
    largest_clique = max(cliques, key=len)
    return largest_clique

def sort_nodes(nodes):
    return sorted(nodes)

adjacency_dict = build_adjacency_dict(data)

# Find all maximal cliques
cliques = find_maximal_cliques(adjacency_dict)

# Find the largest clique
largest_clique = find_largest_clique(cliques)
print("Largest clique:", largest_clique)

# Sort the nodes of the largest clique alphabetically
sorted_largest_clique = sort_nodes(largest_clique)
print("Sorted largest clique:", sorted_largest_clique)

print("SECOND STAR")
print(f"second = {','.join(sorted_largest_clique)}")



