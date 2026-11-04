import pytest
@pytest.mark.skip
def test_demo3(setup):
    driver = setup
    driver.get("https://www.zomato.com/")


@pytest.mark.skip
def test_demo4(setup):
    driver = setup
    driver.get("https://www.swiggy.com/city/bangalore")