# Load Input + Parse into Lists
reports = []

safe_reports = 0

with open("input.txt", "r") as file:
    for line in file:
        levels = [int(level) for level in line.split()]

        # baseline: report is safe
        report_is_safe = True
        descending = None

        # Check Safety of Report
        # parse through levels, make sure levels are either all increasing or all decreasing
        # and that the difference between each consecutive level is at least 1 and at most 3
        # I think we break this into a function
        for i in range(len(levels) - 1):
            # diff the numbers, - is descending, + is ascending
            difference = levels[i] - levels[i + 1]

            # check bounds
            if abs(difference) < 1 or abs(difference) > 3:
                report_is_safe = False
                break

            # check ascending/descending
            if descending is None:
                descending = difference < 0
            else:
                local_descending = difference < 0
                if local_descending != descending:
                    report_is_safe = False
                    break

        safe_reports += int(report_is_safe)

        reports.append(levels)

print(safe_reports)


# Considerations:
# - The logic for checking bounds and ascending/descending could be refactored into their own functions
# - This would allow us to use dependency injection to inject different implementations (test, prod)
# - This would be useful for testing or implementing different safety checks, if criteria change
