from typing import List, Tuple
from pathlib import Path


def is_in_bounds(difference: int) -> bool:
    return abs(difference) >= 1 and abs(difference) <= 3


# monotonic here to mean that the pair is either both ascending or both descending
def is_monotonic(difference: int, descending: bool) -> bool:
    # if difference == 0:
    #     return False

    local_descending = difference > 0

    return local_descending == descending or descending is None


def is_safe(difference: int, descending: bool) -> bool:
    return is_monotonic(difference, descending) and is_in_bounds(difference)


def is_report_safe(levels: List[int]) -> Tuple[bool, bool]:
    descending = None
    safe = True
    fault_count = 0

    # hacky way to check if report is descending
    tonicity_check = (
        int(levels[0] - levels[1] > 0)
        + int(levels[1] - levels[2] > 0)
        + int(levels[2] - levels[3] > 0)
        + int(levels[3] - levels[4] > 0)
    )
    descending = tonicity_check >= 3

    i = 0

    while i < len(levels) - 1:
        difference = levels[i] - levels[i + 1]

        if not is_safe(difference, descending):
            safe = False

            if fault_count > 0:
                return safe, False

            # if last level, can skip safely
            if i + 2 >= len(levels):
                return safe, True

            skip_difference = levels[i] - levels[i + 2]
            # skip current: first index
            next_skip_difference = levels[i + 1] - levels[i + 2]

            # if current and skip is not safe, and we're not at a skippable first index
            if not is_safe(skip_difference, descending) and not is_safe(
                next_skip_difference, descending
            ):
                return safe, False

            fault_count += 1

            # skip next check
            i += 1

        i += 1

    return safe, True


def count_safe_reports(filename: str) -> Tuple[int, int]:
    count = 0
    tolerant_count = 0

    with open(filename, "r") as file:
        for line in file:
            levels = [int(level) for level in line.split()]

            safety_result = is_report_safe(levels)

            if safety_result[1] and not safety_result[0]:
                print(levels)

            count += int(safety_result[0])
            tolerant_count += int(safety_result[1])

    return count, tolerant_count


if __name__ == "__main__":
    script_dir = Path(__file__).parent
    safe_reports = count_safe_reports(script_dir / "input.txt")

    print(safe_reports[0], safe_reports[1])
