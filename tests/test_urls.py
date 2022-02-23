import sys
import time
import json
from typing import List
from urllib import request


# Spoofing with randomly chosen user agent to circumnavigate robot defenses
USER_AGENT = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
HEADERS = {"User-Agent": USER_AGENT}
PATH_TO_DESCRIPTIONS = "../src/assets/descriptions.json"
OBEY_SPEED_LIMIT = True  # To avoid rate limiting


def print_progress_bar(iteration: int, total: int) -> None:
    bar_length = 30
    percent = f"{(int(100 * iteration / total)):d}"
    progress = int(bar_length * iteration // total)
    bar = "=" * (progress - 1) + ">" + " " * (bar_length - progress)
    print(f"\r|{bar}| {percent}%", end="\r")
    sys.stdout.flush()


def read_in_data() -> dict:
    test_preface = "-----------------\nStarting URL Test"
    print(test_preface)
    with open(PATH_TO_DESCRIPTIONS) as f:
        course_descriptions: dict = json.load(f)
    return course_descriptions


def visit_urls(course_descriptions, verbose=True) -> dict:

    if verbose:
        print("Visiting URLs...")

    results = dict()
    total_iterations = len(course_descriptions.keys())
    current_iteration = 0

    for key in course_descriptions.keys():
        current_iteration += 1

        if verbose:
            print_progress_bar(current_iteration, total_iterations)

        for course in course_descriptions[key]["courses"]:
            success = False

            try:
                if OBEY_SPEED_LIMIT:
                    time.sleep(0.01)

                req = request.Request(course["url"], None, HEADERS)
                res = request.urlopen(req)
                success = True
            except:
                pass

            course_name = course["institution"] + "-" + key
            while course_name in results:
                course_name += "-"  # Simple naming scheme to differentiate duplicates

            result = {
                "title": course_name,
                "status": res.status
                if success
                else "couldn't open url: "
                + course["url"]
                + ". Error: "
                + str(sys.exc_info()),
            }
            results[course["url"]] = result
    return results


def print_broken_urls(failed, total) -> None:
    success = len(failed) == 0
    if success:
        print("\nPASS: All URLs seem to be working.")
    else:
        print(f"\nFAIL: {len(failed)} out of {total} urls failed.")

    for i, item in enumerate(failed):
        failure_string = f"    {i + 1}. {item['title']} - STATUS: {item['status']}"
        print(failure_string)


def tally_results(results) -> List:
    total = len(results)
    failed = []
    for item in results.values():
        if item["status"] != 200:
            failed.append(item)

    print_broken_urls(failed, total)
    print("URL Test Complete\n-----------------")

    return failed


if __name__ == "__main__":
    course_descriptions = read_in_data()
    results = visit_urls(course_descriptions)
    failed = tally_results(results)
