#!/usr/bin/env bash
echo "run docker compose"
docker-compose -f docker-compose-v3.yml up

echo "run requirements"
pip install -r ./requirements.txt

echo "start run pytest"
pytest -m smoke
