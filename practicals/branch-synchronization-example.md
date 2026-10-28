# Branch synchronization example

This note records the branch state used for the fetch and pull demonstration.

1. `git fetch origin` refreshes the remote-tracking branch while leaving the checked-out files unchanged.
2. Compare the current commit with the fetched remote tip using `git log --oneline HEAD..origin/practicals/ci-gitops`.
3. Use `git pull --ff-only` to fast-forward this branch when it has no divergent local commits.
4. Verify the updated working tree with `git status --short --branch`.

The demonstration uses the practical branch. It does not update `main`.
