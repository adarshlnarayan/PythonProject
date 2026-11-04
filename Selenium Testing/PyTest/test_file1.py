import pytest
def test_demo1(setup):
    driver = setup
    driver.get("https://demoapps.qspiders.com/ui?scenario=1")



@pytest.mark.skip
def test_demo2(setup):
    driver = setup
    driver.get("https://testautomationpractice.blogspot.com/")
