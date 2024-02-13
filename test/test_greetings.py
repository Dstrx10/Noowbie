import yaml
import pytest
from greetings import greet

def load_test_cases():
    """
    Load test cases from a YAML file.
    """
    with open("test_cases.yaml", "r") as file:
        return yaml.safe_load(file)

@pytest.mark.parametrize("name,expected_output", load_test_cases())
def test_greet(name, expected_output, capsys):
    """
    Test the greet function.
    """
    greet(name)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output.strip()

