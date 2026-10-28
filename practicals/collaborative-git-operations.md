# Collaborative Git operations

Repository: `sgshiv001/github-practical-assignment`

## Safe feature branch flow

```bash
git status --short --branch
git fetch origin
git switch -c feature/my-change origin/main
# edit and review the files
git diff
git add <files>
git commit -m "Describe the change"
git push -u origin feature/my-change
```

Open a pull request from the feature branch to `main`. Review the diff, ask a collaborator for an independent review, address comments, and merge only when the required checks and reviews are complete.

## Fetch and pull

`git fetch origin` updates remote-tracking references without changing the current branch or working files. `git pull --ff-only` fetches and fast-forwards the current branch when possible. If local and remote work diverges, inspect the graph and choose a merge or rebase deliberately.

## Evidence note for this repository

Pull request #2 is an open practical example with passing checks. The recorded comment is an author self-review, not an independent collaborator approval. Pull request #1 has no submitted reviews. Request a peer review before treating either change as independently reviewed or merging it.
