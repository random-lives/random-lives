#!/bin/bash
cd /Users/damonbinder/Documents/RandomLivesWebsite

# These agents read story files, which are untrusted input: a story body can carry
# instructions aimed at the agent reviewing it. Run with acceptEdits, NOT with
# --dangerously-skip-permissions. acceptEdits lets the review edit story files without
# prompting while the allow/ask/deny rules in .claude/settings.local.json still apply,
# so an injected command fails instead of running unattended.
ls _lives/*.md | grep -v REVIEW_LOG | grep -E '/0(07[0-9]|08[0-9]|09[0-9]|1[0-9]{2}|2[0-4][0-9])-' | sort | \
xargs -P 20 -I {} claude --print --permission-mode acceptEdits -p "Review {} following the review-stories skill. Edit the file to fix issues and add a changelog."
