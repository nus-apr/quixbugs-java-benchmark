import os
from os.path import join
from pprint import pprint
import shutil
import json

projects = """bitcount
breadth_first_search*
bucketsort
depth_first_search*
detect_cycle*
find_first_in_sorted
find_in_sorted
flatten
gcd
get_factors
hanoi
is_valid_parenthesization
kheapsort
knapsack
kth
lcs_length
levenshtein
lis
longest_common_subsequence
max_sublist_sum
mergesort
minimum_spanning_tree*
next_palindrome
next_permutation
pascal
possible_change
powerset
quicksort
reverse_linked_list*
rpn_eval
shortest_path_length*
shortest_path_lengths*
shortest_paths*
shunting_yard
sieve
sqrt
subsequences
to_base
topological_ordering*
wrap""".split(
    "\n"
)

result = []
id = 0
if not os.path.exists("java_programs"):
    os.mkdir("java_programs")
os.chdir("java_programs")
root_project = os.getcwd()
for project in projects:
    is_graph_based = project.endswith("*")
    id += 1
    name = project if not is_graph_based else project[:-1]
    file_name = name.upper() + ".java"
    test_file_name = name.upper() + "_TEST" + ".java"
    root = "/home/mmirchev/QuixBugs"
    file = join(root, "java_programs", file_name)
    tests = join(root, "java_testcases", "junit", test_file_name)
    os.mkdir(name)
    os.chdir(name)
    java_folder = "java_programs"
    os.mkdir(java_folder)
    os.makedirs("java_testcases/junit")
    shutil.copy(file, join(".", java_folder, ""))
    if is_graph_based:
        shutil.copy(join(root, java_folder, "Node.java"), join(".", java_folder, ""))
        shutil.copy(
            join(root, java_folder, "WeightedEdge.java"), join(".", java_folder, "")
        )

    f = open(tests, "r")

    neg_tests = f.read().count("Test")

    f.close()

    shutil.copy(
        join(root, "java_testcases", "junit", "QuixFixOracleHelper.java"),
        "./java_testcases/junit/",
    )
    shutil.copy(tests, "./java_testcases/junit/")

    result.append(
        {
            "id": id,
            "subject": "java_programs",
            "bug_id": name,
            "source_file": file_name,
            "source_directory": "src/main/java",
            "class_directory": "target/classes",
            "test_directory": "src/test/java",
            "test_class_directory": "target/test-classes",
            "line_numbers": [],
            "dependencies": [],
            "passing_test_identifiers": [],
            "failing_test_identifiers": [],
            "language": "java",
            "test_timeout": 5,
            "count_neg": neg_tests,
            "count_pos": 0,
        }
    )
    os.chdir(root_project)

os.chdir(join(root_project, ".."))
x = open("meta-data.json", "w")
x.write(json.dumps(result, indent=4))
x.close()
