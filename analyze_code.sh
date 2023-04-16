report_file=analyze_code.report.txt

FILE_LIST=$(find src -type f -iname "*.py" -printf '%p ')

echo Analyzing with MYPY
echo ==== MYPY ==== >${report_file}
echo "(Disable false positives with inline comment '# type: ignore[<ERROR_NAME>]')" >>${report_file}
mypy $FILE_LIST >>${report_file}

echo Analyzing with BANDIT
echo ==== BANDIT ==== >>${report_file}
echo "(Disable false positives with inline comment '# nosec <ERROR_CODE>')" >>${report_file}
bandit --skip=B404,B603 $FILE_LIST 1>>${report_file} 2>NUL

echo Analyzing with PYLINT
echo ==== PYLINT ==== >>${report_file}
pylint --disable=C0301,C0103,R0912,R0913,R0914,R0915 $FILE_LIST >>${report_file}

echo Analyzing with FLAKE8
echo ==== FLAKE8 ==== >>${report_file}
flake8 --extend-ignore=E203,E221,E501 $FILE_LIST >>${report_file}
