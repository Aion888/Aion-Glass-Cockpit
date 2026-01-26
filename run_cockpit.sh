#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
source aion_env/bin/activate
lsof -tiTCP:8051 -sTCP:LISTEN | xargs -r kill -9 || true || true
nohup ./aion_env/bin/python -m pm_app.cockpit </dev/null > logs/cockpit_8051.log 2>&1 &
disown
sleep 1
curl -s -o /dev/null -w "cockpit /_dash-layout -> %{http_code}\n" http://127.0.0.1:8051/_dash-layout || true
tail -n 8 logs/cockpit_8051.log || true
