#!/usr/bin/env bash
set -euo pipefail
python scripts/update_framework_spec_trees.py
python scripts/pm_drift_check.py
rm -f data/pm_drift_report.csv

echo "✅ Daily sync complete"
