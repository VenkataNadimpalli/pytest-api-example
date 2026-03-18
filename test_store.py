import api_helpers
import pytest
'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''


@pytest.fixturea
def another_order():
    payload = {"pet_id": 0}
    response = api_helpers.post_api_data("/store/order", payload)
    assert response.status_code == 201
    return response.json()["id"]


def test_patch_order_by_id(another_order):
    test_endpoint = f"/store/order/{another_order}"
    payload = {"status": "sold"}
    response = api_helpers.patch_api_data(test_endpoint, payload)

    assert response.status_code == 200
    body = response.json()
    print("patch_message:", body)
