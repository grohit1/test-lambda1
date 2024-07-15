import json
import unittest
from handler import handler

class TestLambdaFunction(unittest.TestCase):

    def test_handler(self):
        """
        Test the handler function to see if it returns the correct response
        """
        expected_response = {
            'statusCode': 200,
            'body': json.dumps({'message': 'Hello, World!'}),
            'headers': {'Content-Type': 'application/json'}
        }

        # Call the handler function with empty event and context
        result = handler({}, {})  # Assuming no event and context are needed for this test

        # Check if the result matches the expected response
        self.assertEqual(result, expected_response)

if __name__ == '__main__':
    unittest.main()
