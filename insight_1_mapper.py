#!/usr/bin/env python
# mapper used for insight 4

import sys
import csv

# Increase field size limit for safety
csv.field_size_limit(sys.maxsize)

reader = csv.reader(sys.stdin)

# Skip header row safely (Python 2 compatible)
try:
    next(reader)
except StopIteration:
    sys.exit(0)

# Column indices
CLAIM_STATUS_COL = 10
CLAIM_AMOUNT_COL = 3

for line in reader:
    try:
        claim_status = line[CLAIM_STATUS_COL]
        claim_amount = line[CLAIM_AMOUNT_COL]

        # Always emit a Total record
        print "Total\t1,{0}".format(claim_amount)

        # Emit Pending only when status matches
        if claim_status == "Pending":
            print "Pending\t{0}".format(claim_amount)

    except (ValueError, IndexError):
        continue
