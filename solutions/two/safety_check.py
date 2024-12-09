def is_safe(levels: list[int]) -> bool:
    descending = None

    for i in range(len(levels) - 1):
        # diff the numbers, - is descending, + is ascending
        difference = levels[i] - levels[i + 1]

        # check bounds
        if abs(difference) < 1 or abs(difference) > 3:
            return False

        # check ascending/descending
        if descending is None:
            descending = difference < 0
        else:
            local_descending = difference < 0
            if local_descending != descending:
                return False

    return True


def count_safe_reports(filename: str) -> int:
    count = 0

    with open(filename, "r") as file:
        for line in file:
            levels = [int(level) for level in line.split()]

            report_is_safe = is_safe(levels)

            count += int(report_is_safe)

    return count


if __name__ == "__main__":
    safe_reports = count_safe_reports("inputs.txt")

    print(safe_reports)

# Considerations:
# - The logic for checking bounds and ascending/descending could be refactored into their own functions
# - This would allow us to use dependency injection to inject different implementations (test, prod)
# - This would be useful for testing or implementing different safety checks, if criteria change
