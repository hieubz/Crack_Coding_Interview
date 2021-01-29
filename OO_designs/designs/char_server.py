"""
design a chat server, provide details about various backend components, classes,
methods. What would be the hardest problem to solve?
1. scope your problem. Do status messages exist? Do  you support group chat?
2. define the major system components or technologies that would be useful
"""

import unittest


class ChatServer:
    def __init__(self):
        self.users = set()
        self.messages = []

    def join(self, user):
        """
        join a new user to chat group
        :param user:
        :return:
        """
        self.users.add(user)
        for message in self.messages[-8:]:
            # add the 8 latest message of server
            user.send(message)

    def leave(self, user):
        if user in self.users:
            self.users.remove(user)
            # clear user's history
            user.clear_history()

    def send_all(self, user, text):
        message = (user.name, text)
        self.messages.append(message)
        for u in self.users:
            u.send(message)


class User:
    def __init__(self, name):
        self.name = name
        # user's message history
        self.history = []

    def send(self, message):
        self.history.append(message)

    def clear_history(self):
        self.history = []


class Test(unittest.TestCase):
    def test_chat_server(self):
        server = ChatServer()
        hieu = User('Hieu')
        giang = User('Giang')
        hai = User('Hai')
        server.join(hieu)
        server.join(giang)
        self.assertEqual(server.users, {hieu, giang})
        for i in range(12):
            # hieu's history would be added
            server.send_all(hieu, i)

        server.join(hai)
        self.assertEqual(hai.history, [('Hieu', i) for i in range(4, 12)])
        server.send_all(giang, "chay ho Tay de!!!")
        self.assertEqual(hieu.history[-1], giang.history[-1])


if __name__ == '__main__':
    unittest.main()
