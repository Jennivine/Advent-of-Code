from typing import List

with open("day_14.txt") as puzzleInput:
    data = [line.strip() for line in puzzleInput.readlines()]

def parse_input(arr: List[str]):
    polymer_template = arr[0]

    pair_insertion_rules = {}

    for line in arr[2:]:
        pair, insertion, *_ = line.split(" -> ")
        pair_insertion_rules[pair] = insertion

    return polymer_template, pair_insertion_rules


def process(polymer_template, pair_insertion_rules, steps):
    polymer_pairs = dict()
    i = 0

    # build the initial dict of pairs from the template
    while i < len(polymer_template) - 1:
        pair = polymer_template[i] + polymer_template[i+1]
        num = polymer_pairs.get(pair, 0)
        polymer_pairs[pair] = num + 1
        i += 1

    # count the initial occurrences of the elements in the template
    element_occurrences = dict()
    for element in polymer_template:
        element_occurrences[element] = element_occurrences.get(element, 0) + 1

    for step in range(steps):
        # for each step
        #   1) check if the pair exists in polymer_pairs, continue if not
        #   2) create the two new pairs to insert
        #       - insertion rule NN -> C yields X new of pairs NC & CN, where X is number of existing pairs for the rule
        #   3) increment inserted element's count in element_occurrences by the number of existing pairs for this rule
        #   4) increment new_pairs for each new pair (from (2)) by the number of existing pairs for this rule
        #   5) repeat 1 through 4 until all rules processed
        #   6) replace polymer_pairs with new_pais
        new_pairs = dict()
        for pair, insertion in pair_insertion_rules.items():
            existing_pairs = polymer_pairs.get(pair)
            if existing_pairs is None:
                continue

            left, right = pair[0]+insertion, insertion+pair[1]

            # keep track of the new element we've inserted for counting later
            element_occurrences[insertion] = element_occurrences.get(insertion, 0) + existing_pairs

            new_pairs[left] = new_pairs.get(left, 0) + existing_pairs
            new_pairs[right] = new_pairs.get(right, 0) + existing_pairs

        polymer_pairs.clear()
        polymer_pairs = new_pairs

    return polymer_pairs, element_occurrences


def part01(arr: List[str], steps=10):
    polymer_template, pair_insertion_rules = parse_input(arr)

    print("steps:", steps)
    print("polymer template:", polymer_template)
    print("pair insertion rules:", pair_insertion_rules)

    polymer_pairs, element_occurrences = process(polymer_template, pair_insertion_rules, steps=steps)
    print("polymer pairs:", polymer_pairs)
    print("counts:", element_occurrences)

    s = sorted([num for char, num in element_occurrences.items()])

    return s[len(s)-1] - s[0]


def part02(arr: List[str]):
    return part01(arr, steps=40)

print(part01(data))
print(part02(data))
