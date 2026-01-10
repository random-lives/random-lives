#!/bin/bash
# Classify all stories one at a time using headless Claude

# Process _lives directory (0000-0099)
for i in {0..99}; do
  num=$(printf "%04d" $i)
  file=$(ls _lives/${num}-*.md 2>/dev/null | head -1)
  if [ -n "$file" ]; then
    echo "=== Classifying $file ==="
    claude --print "Classify the lifestyle category for the story at $file using the classify-lifestyles skill. Only classify this one story."
  fi
done

# Process _lives_pending directory (0100-0249)
for i in {100..249}; do
  num=$(printf "%04d" $i)
  file=$(ls _lives_pending/${num}-*.md 2>/dev/null | head -1)
  if [ -n "$file" ]; then
    echo "=== Classifying $file ==="
    claude --print "Classify the lifestyle category for the story at $file using the classify-lifestyles skill. Only classify this one story."
  fi
done

echo ""
echo "=== Classification Complete ==="
echo "To find flagged entries: grep 'lifestyle: \"FLAG:' _lives/*.md _lives_pending/*.md"
