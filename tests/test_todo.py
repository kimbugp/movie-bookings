from .basetest import BaseTestCase
import json
import psycopg2


class TestTodo(BaseTestCase):

    def test_create_todo_succeeds(self):
        data = json.dumps({
            'name': 'Go for lunch',
            'description': 'Go for lunch at 1pm'
        })
        response = self.test_client.post(
            '/todo', data=data, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201)

    def test_update_todo_succeeds(self):
        data = json.dumps({
            'name': 'Go for lunch',
            'description': 'Go for lunch at 1pm'
        })
        new_data = json.dumps({
            'name': 'not going',
            'description': 'Go for lunch at 1pm'
        })
        self.test_client.post('/todo', data=data,
                              headers={'Content-Type': 'application/json'})
        response = self.test_client.put(
            '/todo/1', data=new_data, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'not going')

    def test_delete_todo_succeeds(self):
        data = json.dumps({
            'name': 'Go for lunch',
            'description': 'Go for lunch at 1pm'
        })
        self.test_client.post(
            '/todo', data=data, headers={'Content-Type': 'application/json'})
        response = self.test_client.delete(
            '/todo/1', headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Item has been deleted')

    def test_delete_non_existing_todo_fails(self):
        response = self.test_client.delete(
            '/todo/2', headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['error'], 'Not found')

    def test_update_non_existing_todo_fails(self):
        data = json.dumps({
            'name': 'Go for lunch',
            'description': 'Go for lunch at 1pm'
        })
        response = self.test_client.put(
            '/todo/1', data=data, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['error'], 'Not found')
    
    def test_creating_a_table(self):
        from models.todo import Todo
        with self.assertRaises(psycopg2.ProgrammingError):
            string = Todo.create()
            self.db.execute(string,commit=True)
            self.assertEqual(True,True)
