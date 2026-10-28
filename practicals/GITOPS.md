# GitOps practical notes

This example keeps the application's desired state in `ops/desired-state.json`.
Changes are made in Git, reviewed through a pull request, and checked by the
workflow before they are merged. The repository is the versioned source of
truth for the declared state.

The workflow validates the manifest; it does not deploy to a live cluster.
A real reconciler or deployment target would be a separate, explicitly
configured step.
