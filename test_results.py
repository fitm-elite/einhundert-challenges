import junitparser

def main():
    junit_report = junitparser.JUnitXml.fromfile('report.xml')
    
    passed = sum(1 for suite in junit_report for case in suite if case.result._elem is None)
    failed = sum(1 for suite in junit_report for case in suite if case.result and case.result._elem.tag == 'failure')
    
    print(f'Tests passed: {passed}')
    print(f'Tests failed: {failed}')

if __name__ == "__main__":
    main()