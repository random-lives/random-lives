#!/bin/bash
cd /Users/damonbinder/Documents/RandomLivesWebsite

ls _lives/*.md | grep -v REVIEW_LOG | grep -E '/0(07[0-9]|08[0-9]|09[0-9]|1[0-9]{2}|2[0-4][0-9])-' | sort | \
xargs -P 20 -I {} claude --print --dangerously-skip-permissions -p "Review {} following the review-stories skill. Edit the file to fix issues and add a changelog."
