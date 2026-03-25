# bazel_cicd_demo

A minimal Python project demonstrating CI/CD with Bazel and GitHub Actions.

## What it does

- Runs Bazel tests automatically when a pull request is opened against `main`
- Posts a comment on the PR if any tests fail
- Blocks merging until all tests pass

## Project structure

```
.
├── .bazelrc                        # Default Bazel flags
├── .bazelversion                   # Pins Bazel to 8.4.1 (read by Bazelisk)
├── .github/
│   └── workflows/
│       └── ci.yml                  # CI pipeline
├── BUILD.bazel                     # Bazel build and test targets
├── WORKSPACE                       # External dependency declarations
├── hello.py                        # Library under test
└── test_hello.py                   # Unit tests
```

## Running tests locally

```bash
bazel test //... --noenable_bzlmod --enable_workspace
```

## Branch protection setup

The workflow blocks merging by exiting non-zero on failure, but GitHub must be configured to enforce it:

1. Go to **Settings → Branches** and add a ruleset targeting `main`
2. Enable **Require status checks to pass before merging**
3. Add the `test` check (must match the job name in `ci.yml`)
