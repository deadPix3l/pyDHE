import unittest
import socket
import os
from Crypto.Random import atfork
from Crypto.Util.number import bytes_to_long, long_to_bytes

import pyDHE


class DiffieHellmanTests(unittest.TestCase):

    def test_Alice_Bob_Same_Key(self):
        for i in range(100):
            # 100 iterations should test well despite randomness?
            alice = pyDHE.new()
            bob = pyDHE.new()
            alice.update(bob.getPublicKey())
            bob.update(alice.getPublicKey())

            self.assertEqual(bob.getFinalKey(),
                             alice.getFinalKey(),
                             "Alice and Bob have different keys"
                             )

    def test_negotiate(self, group=14):

        server = socket.socket()
        server.bind(('',0))
        server.listen(1)
        port = server.getsockname()[1]

        pid = os.fork()
        atfork()

        # child process - aka, the server
        if pid == 0:
            sock, _  = server.accept()
            server.close()

        # parent - aka, the client
        else:
            sock = socket.socket()
            sock.connect(('', port))
            server.close()

        alice = pyDHE.new(group)
        local_key = alice.negotiate(sock)
        #sock.close()

        if pid == 0:
            sock.send(long_to_bytes(local_key))
            sock.close()
        else:
            os.wait()
            remote_key = bytes_to_long(sock.recv(1024))
            sock.close()
            self.assertEqual(local_key, remote_key, "keys do not match")

    def test_Forgot_update_fail(self):
        self.assertRaises(ValueError, pyDHE.new().getFinalKey)

    # custom parameters (aka not NIST) failures
    def test_nonNIST_str_fail(self):
        self.assertRaises(TypeError, pyDHE.new, group='failure')

    def test_nonNIST_float_fail(self):
        self.assertRaises(TypeError, pyDHE.new, group=5.2)

    def test_nonNIST_invalid_group_fail(self):
        self.assertRaises(KeyError, pyDHE.new, group=100000)

    def test_nonNIST_dict_missing_key_fail(self):
        self.assertRaises(KeyError, pyDHE.new, group={})

    def test_nonNIST_tuple_invalid_length_fail(self):
        self.assertRaises(IndexError, pyDHE.new, group=(3,))

    def test_nonNIST_tuple_with_float_fail(self):
        self.assertRaises(TypeError, pyDHE.new, group=(2.0, 13.0))

    def test_nonNIST_dict_with_str_fail(self):
        self.assertRaises(TypeError, pyDHE.new, group={'p':'fail', 'g': 2})

    def test_nonNIST_noneType_fail(self):
        self.assertRaises(TypeError, pyDHE.new, group=None)

    # Non-NIST parameters Succeeds
    def test_nonNIST_dict(self):
        pass

    def test_nonNIST_tuple(self):
        pass

if __name__ == '__main__':
    unittest.main()
