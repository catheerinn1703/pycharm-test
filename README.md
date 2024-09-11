# Pytest - API testing with Python `requests`
 
[![API Tests with Pytest](https://github.com/ghoshasish99/API-Testing-Pytest/actions/workflows/pytest.yml/badge.svg)](https://github.com/ghoshasish99/API-Testing-Pytest/actions/workflows/pytest.yml)

#### Pytest is a mature full-featured Python testing frame that helps you write and run tests in Python.

#### The `requests` module allows you to send HTTP requests using Python.

## Getting started

* To download and install `pytest`, run this command from the terminal : `pip install pytest`
* To download and install `requests`, run this command from the terminal : `pip install requests`

To ensure all dependencies are resolved in a CI environment, in one go, add them to a `requirements.txt` file.
* Then run the following command : `pip install -r requirements.txt`

To run the testcase, please use `pytest testcase.py::test_create_user

Folder structure: 
1. method will host all post and get that will be used for running the test
2. test_data will host all data that needed to run the method
3. main will host the testcase that will be run

Thank You!
`