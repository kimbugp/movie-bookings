from .basetest import BaseTestCase
import json


class TestTodo(BaseTestCase):
    def test_create_todo_succeeds(self, test_client):
        data = json.dumps(
            {"name": "Go for lunch", "description": "Go for lunch at 1pm"}
        )
        response = test_client.post(
            "/todo", data=data, headers={"Content-Type": "application/json"}
        )
        self.assertEqual(response.status_code, 201)

    def test_get_todo_succeeds(self, test_client):
        data = json.dumps(
            {"name": "Go for lunch", "description": "Go for lunch at 1pm"}
        )
        test_client.post(
            "/todo", data=data, headers={"Content-Type": "application/json"}
        )
        response = test_client.get(
            "/todo/1", headers={"Content-Type": "application/json"}
        )
        self.assertEqual(response.status_code, 200)

    def test_update_todo_succeeds(self, test_client):
        data = json.dumps(
            {"name": "Go for lunch", "description": "Go for lunch at 1pm"}
        )
        new_data = json.dumps(
            {"name": "not going", "description": "Go for lunch at 1pm"}
        )
        test_client.post(
            "/todo", data=data, headers={"Content-Type": "application/json"}
        )
        response = test_client.put(
            "/todo/1",
            data=new_data,
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], "not going")

    def test_delete_todo_succeeds(self, test_client):
        data = json.dumps(
            {"name": "Go for lunch", "description": "Go for lunch at 1pm"}
        )
        test_client.post(
            "/todo", data=data, headers={"Content-Type": "application/json"}
        )
        response = test_client.delete(
            "/todo/1", headers={"Content-Type": "application/json"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "Item has been deleted")

    def test_delete_non_existing_todo_fails(self, test_client):
        response = test_client.delete(
            "/todo/2", headers={"Content-Type": "application/json"}
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["error"], "Not found")

    def test_update_non_existing_todo_fails(self, test_client):
        data = json.dumps(
            {"name": "Go for lunch", "description": "Go for lunch at 1pm"}
        )
        response = test_client.put(
            "/todo/100",
            data=data,
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["error"], "Not found")
