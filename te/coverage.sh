rm -rf app_data/test_coverage_report
coverage erase; coverage run manage.py test -v 2; coverage html
open app_data/test_coverage_report/index.html
