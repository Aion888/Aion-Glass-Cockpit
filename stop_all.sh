#!/usr/bin/env bash
set +e
lsof -tiTCP:8050 -sTCP:LISTEN | xargs -r kill -9
lsof -tiTCP:8051 -sTCP:LISTEN | xargs -r kill -9
echo "stopped 8050 and 8051"
