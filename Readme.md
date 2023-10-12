Pytest allows you to run a subset of tests in several ways:

| subject                        | Syntax                                              |
|:-------------------------------|-----------------------------------------------------|
| Single test method             | pytest path/test_module.py::TestClass::test_method  |
| All tests in a class           | pytest  path/test_module.py::TestClass              |
| Single test function           | pytest  path/test_module.py::test_function          |
| All tests in a module          | pytest  path/test_module.py                         |
| All tests in a directory       | pytest  path                                        |

Tests matching a name pattern pytest -k pattern
Tests by marker covered in Chapter 6. Markers, on page 73.