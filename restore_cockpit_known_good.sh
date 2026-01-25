#!/bin/zsh
set -e
cd ~/aion
LATEST=$(ls -1t pm_app/cockpit.py.KNOWN_GOOD_* | head -n 1)
echo "Restoring from: $LATEST"
cp "$LATEST" pm_app/cockpit.py
./aion_env/bin/python -m py_compile pm_app/cockpit.py
lsof -tiTCP:8051 -sTCP:LISTEN | xargs -r kill -9 || true
nohup ./aion_env/bin/python -m pm_app.cockpit </dev/null > logs/cockpit_8051.log 2>&1 &
disown
sleep 1
curl -s -o /dev/null -w "LAYOUT %{http_code}\n" http://127.0.0.1:8051/_dash-layout || true
