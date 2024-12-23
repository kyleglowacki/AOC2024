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


def next_secret_number(secret):
    # Step 1: Multiply by 64, mix, and prune
    secret = (secret ^ (secret * 64)) % 16777216
    
    # Step 2: Divide by 32, mix, and prune
    secret = (secret ^ (secret // 32)) % 16777216
    
    # Step 3: Multiply by 2048, mix, and prune
    secret = (secret ^ (secret * 2048)) % 16777216
    
    return secret

def compute_2000th_secret(data):
    total_sum = 0
    for initial_secret in data:
        secret = initial_secret
        for _ in range(2000):
            secret = next_secret_number(secret)
        total_sum += secret
    return total_sum

raw = aocd.get_data(day=22, year=2024)

data = raw.splitlines()
data = convert_string_to_int(data)
#print(data)

result = compute_2000th_secret(data)

print("FIRST STAR")
print(f"first total = {result}")

from itertools import product

def generate_prices(secret, num_prices):
    prices = []
    for _ in range(num_prices):
        secret = next_secret_number(secret)
        prices.append(secret % 10)
    return prices

def precompute_prices_and_changes(data):
    all_prices = []
    all_changes = []
    for initial_secret in data:
        prices = generate_prices(initial_secret, 2001)  # Generate 2001 prices to get 2000 changes
        changes = [prices[i + 1] - prices[i] for i in range(2000)]
        all_prices.append(prices)
        all_changes.append(changes)
    return all_prices, all_changes

def precompute_sequence_positions(all_changes):
    sequence_positions = []
    for changes in all_changes:
        positions = {}
        for i in range(len(changes) - 3):
            seq = tuple(changes[i:i + 4])
            if seq not in positions:
                positions[seq] = i
        sequence_positions.append(positions)
    return sequence_positions

def find_best_sequence(data):
    all_possible_sequences = list(product(range(-9, 10), repeat=4))

    # This was taking over a second per iteration of the 130321 items
    # Compute these outside the loop sped it up 1000 fold
    all_prices, all_changes = precompute_prices_and_changes(data)
    sequence_positions = precompute_sequence_positions(all_changes)
    
    max_bananas = 0
    best_sequence = None

    # Ugh, this still takes too long.. I'd love to move the zip out
    # but I'm not sure how to iterate on whatever it is.
    for idx,sequence in enumerate(all_possible_sequences):
        #print(f"{idx} = {sequence}")
        total_bananas = 0
        
        for prices, positions in zip(all_prices, sequence_positions):
            if sequence in positions:
                total_bananas += prices[positions[sequence] + 4]
        
        if total_bananas > max_bananas:
            max_bananas = total_bananas
            best_sequence = sequence
    
    return best_sequence, max_bananas


best_sequence, max_bananas = find_best_sequence(data)
print(f"Best sequence: {best_sequence}, Max bananas: {max_bananas}")

print("SECOND STAR")
print(f"second = {max_bananas}")



