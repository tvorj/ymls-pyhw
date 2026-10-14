# Python homework

This repository publishes homework in weekly releases. Week 1 contains 13 tasks
with starter code and public tests. Work in your own copy, run tests on your
computer, and save your solutions with Git.

Start with [SETUP.md](SETUP.md) for creating your personal repository, installing
dependencies, testing, committing, pushing, and receiving later homework.
Manytask registration and access to the original SHAD GitLab are not required.

## Week 1

| Group | Task | Practice |
| --- | --- | --- |
| Onboarding | [hello_world](01.1.PythonTools/tasks/hello_world/README.md) | Return a string; run the first test |
| Onboarding | [testlib_test](01.1.PythonTools/tasks/testlib_test/README.md) | Add two numbers; verify testlib installation |
| Core | [fizz_buzz](01.2.BasicTypes/tasks/fizz_buzz/README.md) | Conditions, divisibility, and result lists |
| Core | [iterate_me](01.2.BasicTypes/tasks/iterate_me/README.md) | Nine functions on values and indices |
| Core | [middle_value_of_triple](01.2.BasicTypes/tasks/middle_value_of_triple/README.md) | Comparisons and the middle value |
| Core | [reverse_list](01.2.BasicTypes/tasks/reverse_list/README.md) | Five variants; mutation versus a new list |
| Core | [merge_lists](01.2.BasicTypes/tasks/merge_lists/README.md) | Merge sorted lists |
| Core | [filter_list_by_list](01.2.BasicTypes/tasks/filter_list_by_list/README.md) | Filter sorted lists |
| Core | [bin_basic](01.2.BasicTypes/tasks/bin_basic/README.md) | Binary search |
| Core | [make_assert](01.2.BasicTypes/tasks/make_assert/README.md) | Assertions and CTR calculations |
| Advanced | [common_type](01.2.BasicTypes_hard/tasks/common_type/README.md) | Choose a common type |
| Advanced | [common_type_2](01.2.BasicTypes_hard/tasks/common_type_2/README.md) | Convert mixed data and handle missing values |
| Advanced | [bin_tricky](01.2.BasicTypes_hard/tasks/bin_tricky/README.md) | Median of two sorted sequences |

Start with the onboarding tasks, then the core tasks. The advanced group needs
additional preparation in conversions and algorithms; ask your instructor when
to attempt it. The median task requires more than familiarity with Python syntax.

Each task directory contains:

- `README.md`: requirements and restrictions.
- `<task>.py`: starter code to implement; preserve names, signatures, and docstrings.
- `test_public.py`: public tests to run locally.

## Run a task's tests

After completing setup, run this from the repository root:

```sh
python -m pytest 01.1.PythonTools/tasks/hello_world/test_public.py -v
```

An unfinished starter is expected to fail tests. After implementing it, run the
same command again. Tests check both results and some implementation restrictions.

Local checks provide feedback. Pushing saves your work in your repository;
it does not automatically run a school grader or record a score. The instructor
will announce the review/submission procedure separately.

Original task statements retain references to the SHAD submission system. For
this course, use this repository's setup instructions instead. Source attribution
and export details are in [SOURCE.md](SOURCE.md).
