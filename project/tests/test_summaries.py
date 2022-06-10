import json


def test_create_summary(test_app):
    # given
    # when
    response = test_app.post("/summaries/", data=json.dumps({"url": "https://foo.bar"}))
    # then
    assert response.status_code == 201
    assert response.json()["url"] == "https://foo.bar"


def test_create_summaries_invalid_json(test_app):
    # given
    # when
    response = test_app.post("/summaries/", data=json.dumps({}))
    # then
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "url"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }


def test_read_summary(test_app):
    # given
    response = test_app.post("/summaries/", data=json.dumps({"url": "https://foo.bar"}))
    summary_id = response.json()["id"]
    # when
    response = test_app.get(f"/summaries/{summary_id}/")
    # then
    assert response.status_code == 200
    response_dict = response.json()
    assert response_dict["id"] == summary_id
    assert response_dict["url"] == "https://foo.bar"
    assert response_dict["summary"]
    assert response_dict["created_at"]


def test_read_summary_incorrect_id(test_app):
    # given
    response = test_app.post("/summaries/", data=json.dumps({"url": "https://foo.bar"}))
    summary_id = response.json()["id"] + 1
    # when
    response = test_app.get(f"/summaries/{summary_id}/")
    # then
    assert response.status_code == 404
    assert response.json()["detail"] == f"TextSummary with id {summary_id} not found."


def test_read_all_summaries(test_app):
    # given
    response = test_app.post("/summaries/", data=json.dumps({"url": "https://foo.bar"}))
    summary_id = response.json()["id"]
    # when
    response = test_app.get("/summaries/")
    # then
    assert response.status_code == 200
    response_list = response.json()
    assert len(list(filter(lambda d: d["id"] == summary_id, response_list))) == 1
