#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
source aion_env/bin/activate
{ lsof -tiTCP:8050 -sTCP:LISTEN 2>/dev/null | xargs kill -9 2>/dev/null; } || true
python scripts/build_index.py || true
nohup ./aion_env/bin/python app.py </dev/null > logs/pm_8050.log 2>&1 &
disown
sleep 1
curl -s -o /dev/null -w "pm /_dash-layout -> %{http_code}\n" http://127.0.0.1:8050/_dash-layout || true
tail -n 8 logs/pm_8050.log || true
