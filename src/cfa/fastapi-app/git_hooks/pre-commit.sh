#!/bin/sh

echo "Linting Code"
autopep8 --exit-code -i -r .

exit_code=$?

if [ $exit_code -eq 1 ]; then
    echo "Linting Failed"
elif [ $exit_code -eq 2 ]; then
    echo "Linter edited at least one file. Please check repository and add new changes"
fi

exit $exit_code
