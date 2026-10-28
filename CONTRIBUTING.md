# Contribution Workflow

Use a feature branch for each change so that it can be discussed before it reaches `main`.

1. Fetch the latest remote references with `git fetch origin`.
2. Update the local base branch with `git switch main` and `git pull --ff-only origin main`.
3. Create a branch with `git switch -c feature/short-description`.
4. Make a focused change, then stage and commit it with a clear message.
5. Push the branch with `git push -u origin feature/short-description`.
6. Open a pull request into `main`. Explain the change and include test results.
7. Ask a collaborator to review the diff. Address comments in follow-up commits and wait for approval before merging.

Fetching updates remote-tracking references without changing the current branch. Pulling fetches and integrates a selected remote branch into the current branch. Pushing sends local commits to the remote repository.
