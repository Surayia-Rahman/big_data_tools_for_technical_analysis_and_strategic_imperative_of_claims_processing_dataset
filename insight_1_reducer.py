#!/usr/bin/env python
# for insight 4

import sys

pending_count = 0
pending_amount = 0.0
total_count = 0
total_amount = 0.0

for line in sys.stdin:
    try:
        key, value = line.strip().split('\t', 1)

        if key == "Total":
            count, amount = value.split(',', 1)
            total_count += int(count)
            total_amount += float(amount)

        elif key == "Pending":
            pending_count += 1
            pending_amount += float(value)

    except (ValueError, IndexError):
        continue

# Safe percentage calculations
pct_claims_pending = 0.0
pct_exposure_pending = 0.0

if total_count > 0:
    pct_claims_pending = (float(pending_count) / float(total_count)) * 100

if total_amount > 0:
    pct_exposure_pending = (pending_amount / total_amount) * 100

# Final Report (Python 2 SAFE)
print "--- MapReduce Job Final Report ---"
print ""
print "--- Raw Counts ---"
print "PendingClaimCount:\t{0}".format(pending_count)
print "TotalClaimCount:\t{0}".format(total_count)
print ""
print "--- Raw Financials ---"
print "PendingTotalAmount:\t{0:.2f}".format(pending_amount)
print "TotalExposure:\t\t{0:.2f}".format(total_amount)
print ""
print "--- FINAL INSIGHTS ---"
print "Pending Backlog Rate (by Count):\t{0:.1f}%".format(pct_claims_pending)
print "Pending Backlog Rate (by Value):\t{0:.1f}%".format(pct_exposure_pending)
print "---"
