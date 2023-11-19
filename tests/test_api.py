import unittest
from openai_api import assistant
from openai_api import chat


def abc():
    print(123)


def test_api111():
    msg = chat.send_msg("你好呀")

    print(msg)
    print(msg.content)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here


def assistant_test():
    message_list = assistant.get_thread_by_id('thread_9s3MhO8HhGAmGb5tlOtrdNWw')
    for msg in message_list:
        print(type(msg))


if __name__ == '__main__':
    unittest.main()
