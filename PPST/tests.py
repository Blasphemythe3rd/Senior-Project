from django.test import TestCase
from datetime import datetime
from django.urls import reverse
from django.http import JsonResponse
from unittest.mock import patch
from unittest.mock import MagicMock
from .models import User, Test, Stimuli_Response, Notification, Doctor
from . import views
import json

# Create your tests here.

class NotificationTestCase(TestCase):

    def setUp(self):

        self.user = User.objects.create(username='testuser', email='testuser@example.com')

        self.doctor = Doctor.objects.create(
            first_name='Alice',
            last_name='Smith',
            email='alice.smith@hospital.com',
            username='doctor0'
        )

        # Create a test test object
        self.test = Test.objects.create(
            test_id=123, 
            time_ended='2025-04-02 10:00:00',
            patient_age=30,
            doctor=self.doctor
            )

        # Create a test Stimuli_Response object for the test
        Stimuli_Response.objects.create(test=self.test, response_per_click=1)

    @patch('PPST.views.User.objects.get')
    @patch('PPST.views.Test.objects.get')
    @patch('PPST.views.Stimuli_Response.objects.filter')
    def test_create_notification_test_completed_success(self, mock_stimuli_response, mock_test_get, mock_user_get):
        # Mock the Test object fetch
        mock_test_get.return_value = self.test

        # Mock the Stimuli_Response filter to return the correct completion time
        mock_stimuli_response.return_value.exists.return_value = True

        mock_stimuli_response.return_value.values.return_value.first.return_value = {"test__time_ended": "2025-04-02 10:00:00"}


        # Mock the User object fetch
        mock_user_get.return_value = self.user

        # Prepare the payload
        payload = {
            'user_id': self.user.id,
            'test_id': self.test.test_id,
        }

        # Make a POST request to the view
        response = self.client.post(reverse('PPST:create_notification_test_completed'), json.dumps(payload), content_type='application/json')

        # Print for debugging purposes (optional)
        print(response.status_code)
        print(response.content)

        # Check that the response is valid
        data = json.loads(response.content)
        print(data)

        # Assert that the response is successful
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsNotNone(data['notification_id'])

        # Check that the notification was created and is associated with the doctor
        notification = Notification.objects.get(id=data['notification_id'])
        self.assertIn(self.doctor, notification.users.all())

        # Check that the notification message is correct
        self.assertEqual(notification.message, "Test Id 123 has been completed at 2025-04-02 10:00:00.")

        
    @patch('PPST.views.User.objects.get')
    @patch('PPST.views.Test.objects.get')
    @patch('PPST.views.Stimuli_Response.objects.filter')

    def test_create_notification_test_not_completed(self, mock_stimuli_response, mock_test_get, mock_user_get):
        # Mock the Test object fetch
        mock_test_get.return_value = self.test

        # Mock the Stimuli_Response filter to return no data
        mock_stimuli_response.return_value.exists.return_value = False

        # Prepare the payload
        payload = {
            'test_id': self.test.test_id,
        }

        # Make a POST request to the view
        response = self.client.post(reverse('PPST:create_notification_test_completed'), json.dumps(payload), content_type='application/json')

        # Check the response for the error message
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'Invalid request method.')

    @patch('PPST.views.User.objects.get')
    @patch('PPST.views.Test.objects.get')
    @patch('PPST.views.Stimuli_Response.objects.filter')
    def test_create_notification_invalid_request(self, mock_stimuli_response, mock_test_get, mock_user_get):
        # Prepare an invalid payload (missing user_id)
        payload = {
            'test_id': self.test.test_id,
        }

        # Make a POST request to the view
        response = self.client.post(reverse('PPST:create_notification_test_completed'), json.dumps(payload), content_type='application/json')

        # Check the response for the error message
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'Invalid request method.')

    @patch('PPST.views.User.objects.get')
    @patch('PPST.views.Test.objects.get')
    @patch('PPST.views.Stimuli_Response.objects.filter')
    def test_create_notification_test_not_found(self, mock_stimuli_response, mock_test_get, mock_user_get):
        # Simulate that Test object doesn't exist
        mock_test_get.side_effect = Test.DoesNotExist

        # Prepare the payload
        payload = {
            'user_id': self.user.id,
            'test_id': 99999,  # Non-existent test ID
        }

        # Make a POST request to the view
        response = self.client.post(reverse('PPST:create_notification_test_completed'), json.dumps(payload), content_type='application/json')

        # Check the response for the error message
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 'Test matching query does not exist.')
