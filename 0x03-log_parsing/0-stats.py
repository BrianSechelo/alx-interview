#!/usr/bin/python3
""" Module Doc """
import sys

def print_stats(total_size, status_counts):
    """Prints the current file size and status code counts."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")

total_size = 0
status_counts = {}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue

        try:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
        except ValueError:
            continue

        total_size += file_size
        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            if status_code not in status_counts:
                status_counts[status_code] = 0
            status_counts[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    raise

print_stats(total_size, status_counts)
