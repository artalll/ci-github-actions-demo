# ci-github-actions-demo
This project demonstrates how to use GitHub Actions for Continuous Integration (CI).
It includes:
- A simple Python function
- A unit test using `unittest`
- A CI workflow that runs on every push to `main`

## Project Structure
main.py # Python file with simple logic
test_main.py # Unit test for the function
.github/
workflows/
ci.yml # GitHub Actions workflow

## Running Tests Locally
Make sure you have Python 3.9+ installed:
python3 test_main.py
