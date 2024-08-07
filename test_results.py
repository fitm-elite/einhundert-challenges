from junitparser import JUnitXml

def __unit_testing__(filename: str) -> tuple[int, int]:
    """
    Counts the total number of passed and failed tests in a JUnit XML file.

    Args:
        xml_file: The path to the JUnit XML file.

    Returns:
        The total number of passed tests.
    """
    test_suites = JUnitXml.fromfile(filename)
    
    total_passed: int = 0
    for suite in test_suites:
        for case in suite:
            if not case.result:
                total_passed += 1
    
    total_failures: int = test_suites.failures
    
    return total_passed, total_failures

def main():
    report_filename: str = "report.xml"
    total_passed, total_failures = __unit_testing__(filename=report_filename)
    
    message = f"""
    Edinhundert Challenges (Test set):
    Test set for Computer Programming Problems in the "Student Applications Open For The Coding Skills Program"
    
    🌱 Tests passed: {total_passed}
    💥 Tests failed: {total_failures}
    """
    print(message)

if __name__ == "__main__":
    main()