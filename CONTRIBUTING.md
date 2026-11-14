# Contributing to ClipForge

Thank you for your interest in contributing to **ClipForge**!

## Development Standards
1. **Branching & Commits**: Use [Conventional Commits](https://www.conventionalcommits.org/) (`feat(vision): ...`, `fix(rendering): ...`, `docs(api): ...`).
2. **Type Safety & Linting**:
   - Frontend: `npx tsc --noEmit` and `npm run lint` must pass with zero warnings/errors.
   - Python Worker: Follow PEP 8 with 100-character line limits (`ruff check local_worker engines tests`).
3. **Testing**:
   - Every bug fix or pipeline change must include unit or integration test coverage under `src/test/`, `local_worker/tests/`, or `tests/`.
   - Never commit API keys, `.env` files, or large binary video files.
