# CS0P_Final_Project_Mini_Data_Analysis_Toolkit

# Mini Data Analyzer

A command-line application for analyzing data from CSV files.

The project allows users to load a CSV dataset and perform basic statistical operations such as calculating the mean, median, mode, standard deviation, minimum and maximum values, frequency, correlation, and normalization.

The project also includes automated tests using `pytest`.

## Features

The application supports the following operations:

| Operation              | Description                                    |
| ---------------------- | ---------------------------------------------- |
| **Mean**               | Calculates the arithmetic mean                 |
| **Median**             | Calculates the median                          |
| **Mode**               | Finds the mode or multiple modes               |
| **Standard deviation** | Calculates the standard deviation              |
| **Min/Max**            | Finds the minimum or maximum value             |
| **Frequency**          | Counts the occurrences of each value           |
| **Correlation**        | Calculates the correlation between two columns |
| **Normalize**          | Normalizes values to a range from `0` to `1`   |
| **Show Dataset**       | Displays the CSV dataset as a table            |
| **Exit**               | Exits the application                          |

## Project Structure

```text
project/
│
├── main.py
├── statistic_library.py
├── csv_handler.py
├── student.csv
├── test_statistic_library.py
└── README.md
```

### `main.py`

The main application file.

It is responsible for:

* starting the application;
* processing command-line arguments;
* displaying the menu;
* selecting operations;
* selecting columns;
* displaying results.

### `statistic_library.py`

Contains the statistical functions:

* `conver_column_to_int()`
* `mean()`
* `median()`
* `mode()`
* `standard_deviation()`
* `minimum()`
* `maximum()`
* `frequency()`
* `correlation()`
* `normalize()`
* `show_dataset()`

### `csv_handler.py`

Responsible for loading CSV files and converting their contents into a dictionary where the keys are column names.

### `test_statistic_library.py`

Contains automated tests for checking the correctness of the statistical functions.

---

## Requirements

The project requires:

* Python 3.10+
* `pytest`
* `tabulate`

Install the dependencies with:

```bash
pip install pytest tabulate
```

Or:

```bash
python -m pip install pytest tabulate
```

---

## Running the Application

The application takes the CSV filename as a command-line argument.

```bash
python main.py student.csv
```

After starting, the following menu will be displayed:

```text
==================
MINI DATA ANALYZER
==================

Dataset: student.csv
Rows: 10
Columns: 4

Choose operation:

1. Mean
2. Median
3. Mode
4. Standart deviation
5. Min/Max
6. Frequency
7. Corelation
8. Normalize
9. Show Dataset
0. Exit

Choice:
```

The user selects an operation by entering its number and then selects the required column.

---

## CSV Format

The application works with standard CSV files containing column headers.

Example:

```csv
Name,Age,Score,Hours
Alice,20,85,10
Bob,21,90,12
Charlie,19,75,8
David,22,95,15
Eve,20,88,11
```

After loading, the data is represented approximately as:

```python
{
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": ["20", "21", "19", "22", "20"],
    "Score": ["85", "90", "75", "95", "88"],
    "Hours": ["10", "12", "8", "15", "11"]
}
```

Numeric values are converted to integers before statistical operations are performed.

---

## Statistical Functions

### `conver_column_to_int(column)`

Converts the values of a column to integers.

```python
conver_column_to_int(["1", "2", "3"])
```

Returns:

```python
[1, 2, 3]
```

If a value cannot be converted to an integer, a `ValueError` is raised.

---

### `mean(column)`

Calculates the arithmetic mean.

```python
mean([1, 2, 3, 4, 5])
```

Returns:

```text
3
```

Formula:

```text
mean = sum(x) / n
```

---

### `median(column)`

Calculates the median of a dataset.

For an odd number of elements, the middle value is returned.

For an even number of elements, the average of the two middle values is returned.

```python
median([1, 2, 3, 4, 5])
```

Returns:

```text
3
```

```python
median([1, 2, 3, 4, 5, 6])
```

Returns:

```text
3.5
```

---

### `mode(column)`

Finds the most frequently occurring value or values.

```python
mode([1, 2, 2, 4, 5, 4, 2])
```

Returns:

```python
[2]
```

If multiple values have the same highest frequency, all of them are returned.

```python
mode([5, 2, 7, 3, 2, 5, 6, 2, 5, 5, 2])
```

Returns:

```python
[5, 2]
```

---

### `standard_deviation(column)`

Calculates the standard deviation.

The project uses the population standard deviation formula:

```text
sqrt(sum((x - mean)²) / n)
```

Example:

```python
standard_deviation([10, 12, 14, 16, 18])
```

Returns approximately:

```text
2.83
```

---

### `minimum(column)`

Returns the minimum value in a column.

```python
minimum([2, 4, 5, 6, 8, 0])
```

Returns:

```text
0
```

---

### `maximum(column)`

Returns the maximum value in a column.

```python
maximum([2, 4, 5, 6, 8, 0])
```

Returns:

```text
8
```

---

### `frequency(column)`

Counts how many times each value occurs.

```python
frequency([2, 2, 4, 5, 2, 4, 1])
```

Returns:

```python
{
    1: 1,
    2: 3,
    4: 2,
    5: 1
}
```

---

### `correlation(first_column, second_column)`

Calculates the Pearson correlation coefficient between two columns.

The coefficient is in the range:

```text
-1 ≤ r ≤ 1
```

General interpretation:

* `r ≈ 1` — strong positive correlation;
* `r ≈ -1` — strong negative correlation;
* `r ≈ 0` — little or no linear correlation.

Example:

```python
correlation(
    [1, 2, 3, 4, 5],
    [2, 3, 5, 4, 7]
)
```

Returns approximately:

```text
0.89
```

If one of the columns contains only identical values, the correlation is undefined and a `ValueError` is raised.

A `ValueError` is also raised if the two columns have different lengths.

---

### `normalize(column)`

Normalizes values to a range from `0` to `1`.

The project uses min-max normalization:

```text
normalized = (x - min) / (max - min)
```

Example:

```python
normalize([10, 20, 30, 40, 50])
```

Returns:

```python
[0.0, 0.25, 0.5, 0.75, 1.0]
```

If all values are identical, normalization is impossible and a `ValueError` is raised.

---

### `show_dataset(dictionary)`

Displays the dataset as a formatted table using the `tabulate` library.

Example:

```text
+--------+-----+-------+
| Name   | Age | Score |
+========+=====+=======+
| Alice  | 20  | 85    |
+--------+-----+-------+
| Bob    | 21  | 90    |
+--------+-----+-------+
```

---

## Error Handling

The application handles common input and data errors.

### Invalid numeric value

```python
conver_column_to_int(["1", "2", "0.1"])
```

Raises:

```text
ValueError
```

### Correlation with a constant column

```python
correlation(
    [5, 5, 5, 5, 5],
    [2, 3, 5, 4, 7]
)
```

Raises:

```text
ValueError: Correlation is undefined for constant rows
```

### Normalization of a constant column

```python
normalize([5, 5, 5, 5])
```

Raises:

```text
ValueError: Cannot normalize a constant row
```

---

## Testing

The project uses `pytest` for automated testing.

Run all tests with:

```bash
pytest
```

For more detailed output:

```bash
pytest -v
```

The tests cover:

* conversion of strings to integers;
* invalid input handling;
* arithmetic mean;
* median;
* mode;
* standard deviation;
* minimum;
* maximum;
* frequency;
* correlation;
* correlation error handling;
* normalization.

Example:

```text
================ test session starts ================

test_statistic_library.py .............           [100%]

================= 13 passed =================
```

---

## Project Architecture

The project is divided into several components:

```text
                 ┌──────────────┐
                 │   main.py    │
                 │  CLI / Menu  │
                 └──────┬───────┘
                        │
             ┌──────────┴──────────┐
             │                     │
             ▼                     ▼
      ┌──────────────┐      ┌────────────────────┐
      │ csv_handler  │      │ statistic_library  │
      │              │      │                    │
      │ CSV Loading  │      │ Statistical        │
      │              │      │ Operations         │
      └──────────────┘      └────────────────────┘
                                    ▲
                                    │
                            ┌───────┴────────┐
                            │     pytest     │
                            │     Tests      │
                            └────────────────┘
```

---

## Example

Suppose the project contains a file called `student.csv`:

```csv
Student,Score
Alice,80
Bob,90
Charlie,70
David,100
Eve,90
```

Run the application:

```bash
python main.py student.csv
```

Select:

```text
2. Median
```

Then select the `Score` column:

```text
1. Student
2. Score

Choice(number): 2
```

The application will calculate the median:

```text
Median value: 90
```

---

## Limitations

The current version has several limitations:

* numeric values must be convertible to `int`;
* floating-point values such as `0.5` are not supported;
* statistical operations are intended for numeric columns;
* the CSV file must contain a header row;
* correlation requires two columns with the same length;
* empty columns are not supported;
* the application uses a command-line interface.
  
---


## Author

**Mini Data Analyzer**

A Python project for learning CSV processing, statistics, command-line interfaces, error handling, and automated testing with `pytest`.
