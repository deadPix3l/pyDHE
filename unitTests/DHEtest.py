import unittest
import socket
from Crypto.Util.number import bytes_to_long, long_to_bytes

import DHE

HOST = ("localhost", 12345)


class DiffieHellmanTests(unittest.TestCase):

    def test_Alice_Bob_Same_Key(self):
        for i in range(100):
            # 100 iterations should test well despite randomness?
            alice = DHE.new()
            bob = DHE.new()
            alice.update(bob.getPublicKey())
            bob.update(alice.getPublicKey())

            self.assertEqual(bob.getFinalKey(),
                             alice.getFinalKey(),
                             "Alice and Bob have different keys"
                             )

    def test_Forgot_update(self):
        alice = DHE.new()
        self.assertRaises(ValueError, alice.getFinalKey)

    def test_negotiate(self, group=14):

        client = socket.socket()
        client.connect(HOST)

        alice = DHE.new(group)
        local_key = alice.negotiate(client)
        remote_key = bytes_to_long(client.recv(1024))
        client.close()

        self.assertEqual(local_key, remote_key, "keys do not match")


def negotiate_server(group=14):
    server = socket.socket()
    server.bind(HOST)
    server.listen(5)
    conn, _ = server.accept()

    alice = DHE.new(group)
    local_key = alice.negotiate(conn)

    conn.send(long_to_bytes(local_key))
    conn.close()


if __name__ == '__main__':
    unittest.main()
