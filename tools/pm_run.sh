#!/usr/bin/env bash
set -euo pipefail

cd /workspaces/Aion-PM

# 1) Refresh (build ALIGNED + MAPPED)
./tools/pm_refresh.sh

# 2) If there are review rows, generate the manual map + stop (so you can edit)
PY="./aion_env/bin/python"
RR=$($PY - <<'PY'
from openpyxl import load_workbook
wb = load_workbook("data/Project_Aion_PM_System_ALIGNED_MAPPED.xlsx", data_only=True)
rr = (wb["Review_Roadmap"].max_row-1) if "Review_Roadmap" in wb.sheetnames else 0
tr = (wb["Review_Tickets"].max_row-1) if "Review_Tickets" in wb.sheetnames else 0
print(max(0, rr+tr))
PY
)

if [[ "${RR}" -gt 0 ]]; then
  echo ""
  echo "⚠️  Review rows detected (${RR}). Generating manual map CSV and stopping so you can edit it:"
  echo "    tools/framework_manual_map.csv"
  echo ""
  ./tools/pm_finalize.sh
  echo ""
  echo "Next:"
  echo "  1) Edit tools/framework_manual_map.csv (framework_node_final column)"
  echo "  2) Re-run: ./tools/pm_run.sh"
  exit 0
fi

# 3) No review rows -> finalize + promote automatically
./tools/pm_finalize.sh
./tools/pm_promote.sh

echo ""
echo "✅ PM run complete. Official workbook updated:"
echo "   data/Project_Aion_PM_System.xlsx"
