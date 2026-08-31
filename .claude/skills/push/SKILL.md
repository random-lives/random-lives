---
name: git-push
description: Adds, commits, and pushes to GitHub. 
---

# Push Skill

When committing and pushing changes, always follow this sequence:

1. `git add .` - Stage all changes
2. `git commit -m "descriptive message"` - Commit with a clear message describing what changed
3. `git push` - Push to remote

Do all three steps without pausing to ask between steps 1 and 2.

`git push` publishes to the public repository that serves the live site, so it always
requires an explicit permission prompt. Wait for that approval — never work around it
(no `--dangerously-skip-permissions`, no alternate command spelling, no push helper
script). If the push is not approved, stop and report that the commit is local only.
