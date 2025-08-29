# ci-github-actions-demo
This project demonstrates how to use GitHub Actions for Continuous Integration (CI) and automation tasks in a Python project.

It includes:
- A simple Python function
- A unit test using `unittest`
- A CI workflow that runs on every push to `main`
- A scheduled workflow that runs daily at midnight UTC
- A matrix build to test the code on multiple Python versions
- A self-hosted runner for executing workflows outside GitHub-hosted machines

## Project Structure
- main.py # Python file with simple logic
- test_main.py # Unit test for the function
- .github/
  - workflows/
    - ci.yml # GitHub Actions workflow
    - scheduled.yml # Scheduled build at midnight
    - matrix-ci.yml       # Matrix testing on multiple Python versions

## CI Workflows Overview
## Part 1: Basic CI Pipeline
- Trigger: On every push to main
  - Steps:
    - Checkout code
    - Set up Python
    - Install dependencies
    - Run unit tests with unittest
    - File: .github/workflows/ci.yml
## Part 2: Advanced GitHub Actions Features
## Cron Scheduling
- Trigger: Every day at 00:00 UTC
  - Purpose: Simulate a nightly job
  - Log Output:
  - Scheduled build completed successfully!
  - File: .github/workflows/scheduled.yml
## Matrix Builds
- Trigger: On push to main
  - Strategy: Tests run in parallel for Python versions:
    - 3.7
    - 3.8
    - 3.9
    - 3.10
    - Goal: Ensure compatibility across multiple Python versions
    - File: .github/workflows/matrix-ci.yml
## Self-Hosted Runner
- A custom runner need to be configured on a local machine.
- Use to execute the basic CI workflow (ci.yml).
- Verify successful run from a non-GitHub-hosted environment.
- Self-Hosted Runner Setup (Summary):
- Register via GitHub UI: Settings → Actions → Runners
- Install and start runner on local machine.
