#!/bin/bash

# Review stories 0000-0039 in parallel using headless Claude
# Run 5 at a time to avoid rate limits

# Story files to review
declare -a STORIES=(
    "_lives/0000-zhang-wei.md"
    "_lives/0001-nagamma.md"
    "_lives/0002-bhima.md"
    "_lives/0003-mercedes-condori-herrera.md"
    "_lives/0004-koitale.md"
    "_lives/0005-tako.md"
    "_lives/0006-nadiia.md"
    "_lives/0007-kandan.md"
    "_lives/0008-mallamma.md"
    "_lives/0009-anandi.md"
    "_lives/0010-hanna.md"
    "_lives/0011-pleuron.md"
    "_lives/0012-kpovi.md"
    "_lives/0013-nathu.md"
    "_lives/0014-hadiya.md"
    "_lives/0015-hormizd.md"
    "_lives/0016-chuku.md"
    "_lives/0017-person-0017-unnamed.md"
    "_lives/0018-vasundhara.md"
    "_lives/0019-sovan.md"
    "_lives/0020-hind.md"
    "_lives/0021-tomi.md"
    "_lives/0022-chikako.md"
    "_lives/0023-paravi.md"
    "_lives/0024-mielo.md"
    "_lives/0025-poda.md"
    "_lives/0026-person-0026-unnamed.md"
    "_lives/0027-pachompsais.md"
    "_lives/0028-peldzom.md"
    "_lives/0029-murugan.md"
    "_lives/0030-targasnalli.md"
    "_lives/0031-eirēnē.md"
    "_lives/0032-nola.md"
    "_lives/0033-mikhail.md"
    "_lives/0034-temir.md"
    "_lives/0035-tatia.md"
    "_lives/0036-vladislav.md"
    "_lives/0037-yang-meiying.md"
    "_lives/0038-tana.md"
    "_lives/0039-ami.md"
)

BATCH_SIZE=5
count=0

for story_file in "${STORIES[@]}"; do
    story_name=$(basename "$story_file")
    echo "Starting review of ${story_name}..."

    # Run claude in headless mode with dangerously-skip-permissions
    claude --dangerously-skip-permissions -p "Review the story at ${story_file} using the review-stories skill. Go through all 14 passes and fix any issues you find." &

    ((count++))

    # Wait for batch to complete before starting next batch
    if (( count % BATCH_SIZE == 0 )); then
        echo "Waiting for batch of $BATCH_SIZE to complete..."
        wait
        echo "Batch complete. Starting next batch..."
    fi
done

# Wait for any remaining jobs
wait
echo "All reviews completed."
