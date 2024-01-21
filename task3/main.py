import os
import timeit
import kmp_search as kmp
import bm_search as bm
import rk_search as rk

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
COLOR_END = '\033[0m'


def compare_algorithms(text, search_term):
    result = dict()
    result["Boyer–Moore search"] = timeit.timeit(
        lambda: bm.boyer_moore_search(text, search_term), number=100)
    result["KMP search"] = timeit.timeit(
        lambda: kmp.kmp_search(text, search_term), number=100)
    result["Rabin-Karp search"] = timeit.timeit(
        lambda: rk.rabin_karp_search(text, search_term), number=100)

    return result


def print_results(results):
    header = f"| {'Algorithm':<20} | {'Execution time':<15} |"
    separator = "| " + "-"*20 + " | " + "-"*15 + " |"
    row_template = "| {key:<20} | {value:^15.5f} |"
    footer = "| " + "-"*38 + " |"

    print(header)
    print(separator)
    for key, value in results.items():
        print(row_template.format(key=key, value=value))
    print(footer)


def load_test_data():
    dir_path = os.path.join(os.getcwd(), "data")
    print(YELLOW + "\nLoading test files paths:" + COLOR_END)
    file_paths = []
    for file in os.listdir(dir_path):
        file_path = os.path.join(os.getcwd(), dir_path, file)
        if os.path.isfile(file_path):
            print(YELLOW + "\tFound file at " + file_path + COLOR_END)
            file_paths.append(file_path)
    if not len(file_paths):
        exit(f"\t{RED}No files found at {dir_path}. Exit.{COLOR_END}")
    return file_paths


def main():

    file_paths = load_test_data()

    # article_1.txt: "позиція" at index 3044; абирвалг at index -1
    # article_2.txt: "позиція" at index 7526; абирвалг at index -1
    search_terms = ["позиція", 'абирвалг']

    print(YELLOW + "\nStarting search alogirhtms time execution comparison..." + COLOR_END)

    for search_term in search_terms:
        for path in file_paths:
            with open(path, 'r', encoding='utf-8') as file:
                text = file.read()
                print(
                    GREEN + f'\nComparing algorithms by searching substring "{search_term}" in file {path}\n' + COLOR_END)
                results = compare_algorithms(text, search_term)
                print_results(results)


if __name__ == "__main__":
    main()
