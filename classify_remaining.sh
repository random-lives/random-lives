#!/bin/bash
# Classify only the remaining stories that don't have old_lifestyle field
# Runs 10 classifications in parallel

MAX_PARALLEL=10
count=0

for file in _lives_pending/*.md; do
  if ! grep -q "old_lifestyle:" "$file" 2>/dev/null; then
    echo "=== Classifying $file ==="
    claude --print --dangerously-skip-permissions "Classify the lifestyle category for the story at $file using the classify-lifestyles skill. Only classify this one story." &

    ((count++))

    # Wait when we hit MAX_PARALLEL running jobs
    if (( count >= MAX_PARALLEL )); then
      wait -n  # Wait for any one job to finish
      ((count--))
    fi
  fi
done

# Wait for all remaining background jobs to finish
wait

echo ""
echo "=== Classification Complete ==="
echo "To find flagged entries: grep 'lifestyle: \"FLAG:' _lives/*.md _lives_pending/*.md"
