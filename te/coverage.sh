rm -rf app_data/test_coverage_report
coverage erase; coverage run manage.py test; coverage html
open app_data/test_coverage_report/index.html
