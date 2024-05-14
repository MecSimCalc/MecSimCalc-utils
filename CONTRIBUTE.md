# Contributing to MecSimCalc

We welcome contributions to MecSimCalc. Please follow the guidelines below. 


## When contributing code to MecSimCalc
When contributing code to MecSimCalc, make sure to:
- Format your code using the black code formatter
- Test your code (or add tests if you are adding a new feature)
- Python 3.6+ is supported
- Include a docstring for each function you add
- Document your code in the README.md file

## How to test your changes
Before submitting a pull request, please make sure that your changes do not break the existing code. You can run the tests by executing the following command in the root directory of the repository:

(You may need to install pytest first by running `pip install pytest`)
```bash
pip install .
```
```bash
pytest .
```

## Code quality
Please make sure that your code follows the PEP 8 style guide and naming conventions. You can correct your fomatting by running the following command in the root directory of the repository:

(You may need to install black first by running `pip install black`)

```bash
black .
```

## Docstrings
Please include a docstring for each function you add. Also include type hints and return type hints.

Docstrings should follow the [numpydoc format](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html). But make sure to include the function with the `>>>` symbol. Here is an example of a docstring:

(Docstrings are shown when users hover over the function. This helps users understand what the function does and how to use it without having to look at the source code.)

```python
def my_function(arg1 : int, arg2 : int) -> int:
    """
    >>> def my_function(arg1 : int, arg2 : int) -> int:

    This is a brief description of the function. This function adds two numbers together.

    Parameters
    ----------
    arg1 : int
        This is a description of arg1.
    arg2 : int
        This is a description of arg2.

    Returns
    -------
    int
        This is a description of the return value.

    Examples
    --------
    >>> my_function(1, 2)
    3
    """
    return arg1 + arg2
```


## Release process
When you are ready to release a new version of MecSimCalc, please follow the steps below:

1. Update the version number in the `setup.py` file
2. Update all references to the version number in the code and documentation before creating a new release (e.g., in the README.md file, update the links to the source code and documentation to point to the new version before creating a new release)
3. Create a new release on GitHub with the updated version number as the tag name

**How to update the links in the README.md file:**
Imagine you want to update your code to version 1.1.2. You would update the links in the README.md file as follows:

Original:
```markdown
...href="https://github.com/MecSimCalc/MecSimCalc-utils/blob/**v0.1.5**/mecsimcalc/general_utils.py#L7C1-L56C61"...
```

Updated:
```markdown
...href="https://github.com/MecSimCalc/MecSimCalc-utils/blob/**v1.1.2**/mecsimcalc/general_utils.py#L7C1-L56C61"...
```

**IMPORTANT: MODIFY THE VERSION BEFORE CREATING A NEW RELEASE**

