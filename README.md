# LeetCodePython

Python solutions for LeetCode problems, organized as a normal `src/`-layout package.

## Structure

```text
src/leetcode_python/
  solutions/
tests/
```

Each problem solution lives in `src/leetcode_python/solutions/` and should have a matching test in
`tests/`.

## Setup

```powershell
.\.venv\Scripts\pip install -e ".[dev]"
```

## Run checks

```powershell
.\.venv\Scripts\pytest.exe -q
.\.venv\Scripts\ruff.exe check .
```
