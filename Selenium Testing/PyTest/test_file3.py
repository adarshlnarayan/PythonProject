import pytest
@pytest.mark.skip
def test_demo5(setup):
    driver = setup
    driver.get("https://www.uber.com/us/en/ride")


@pytest.mark.skip
def test_demo6(setup):
    driver = setup
    driver.get("https://www.olaelectric.com/")
