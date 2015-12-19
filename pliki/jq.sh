#!/bin/bash
cat $1 | jq  -c '.tramos[]| {"type": "Feature","geometry": {"type": "Point", "coordinates": .points | map([.lon,.lat])},"properties":{"name": .name, "id": .id}}' >> $2
