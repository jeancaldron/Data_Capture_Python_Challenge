# Data Capture Python Challenge

This project is a solution to the Data Capture Python challenge. It consists of a Python module `data_capture` containing two classes: `DataCapture` and `Stats`. The `DataCapture` class is used to add numbers and build a `Stats` object which can be queried for statistics about the inputs.

## Project Structure

```
data_capture_python_challenge/
│
├── src/
│   ├── data_capture.py
│   └── __init__.py
│
├── tests/
│   ├── test_data_capture.py
│   └── __init__.py
│
├── requirements.txt
└── README.md
```

## Classes

### DataCapture

#### Methods

- `add(value: int)`: Adds a number to the collection.
- `build_stats() -> Stats`: Builds and returns a `Stats` object for querying statistics about the inputs.

### Stats

#### Methods

- `less(value: int) -> int`: Returns the count of numbers in the collection less than the given value.
- `greater(value: int) -> int`: Returns the count of numbers in the collection greater than the given value.
- `between(low: int, high: int) -> int`: Returns the count of numbers in the collection between the given range.

## Tests

The tests can be found in the `tests` directory.
## Installing Dependencies

1. Navigate to the project root directory.
2. Run the following command to install the required dependencies listed in the `requirements.txt` file:
   
   ```sh
   pip install -r requirements.txt
   ```

## Running Tests with Pytest

1. Ensure that you have installed the dependencies from the `requirements.txt` file.
2. Navigate to the project root directory.
3. Run the following command to execute the tests using `pytest`:

   ```sh
   pytest tests/test_data_capture.py
   ```
