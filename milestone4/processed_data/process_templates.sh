#!/bin/bash

./filter_templates.py
for f in template_position_*; do echo $f; echo $f-sorted; sort -u $f > $f-sorted; mv $f-sorted $f; done
