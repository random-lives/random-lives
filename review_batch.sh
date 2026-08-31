#!/bin/bash
cd /Users/damonbinder/Documents/RandomLivesWebsite

# These agents read story files, which are untrusted input: a story body can carry
# instructions aimed at the agent reviewing it. Run with acceptEdits, NOT with
# --dangerously-skip-permissions. acceptEdits lets the review edit story files without
# prompting while the allow/ask/deny rules in .claude/settings.local.json still apply,
# so an injected command fails instead of running unattended.
echo "_lives/0100-harcharan.md
_lives/0102-nari.md
_lives/0103-nabira.md
_lives/0104-nikhil.md
_lives/0105-frances-mary.md
_lives/0107-guang.md
_lives/0110-hafsa.md
_lives/0111-li-shi.md
_lives/0112-sena.md
_lives/0113-nirmala.md
_lives/0114-ravi.md
_lives/0115-kaushalya.md
_lives/0116-fazal-karim.md
_lives/0117-tiberius.md
_lives/0118-zhao-shun.md" | xargs -P 15 -I {} claude --print --permission-mode acceptEdits -p "Review {} following the review-stories skill. Edit the file to fix issues and add a changelog."
