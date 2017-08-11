# pyDHE

pyDHE is a simple to use Diffie-Hellman implementation written in python, for
python. It makes using Diffie-Hellman a breeze so you can focus on the real
crypto. Eventually, I hope to include elliptic curves (ECDHE) but that is not
currently supported.

## Why?

For several of my other projects, I've needed a Diffie-Hellman-Ephemeral (DHE)
implementation, but could never find one. The algorithm is not hard, but I was
always surprised when I searched for a prewritten one, and never found it.
Even well known Crypto libraries like pyCrypto, pyCryptodome, and cryptography
lacked Diffie-Hellman. So I always write my own. Eventually I decided to make
that terrible code i used previously and generalize it. Make it easy, readable,
pep8 and pep257 compliant, write unit tests and release it to the world!

## How?

Using pyDHE is a breeze. There are two modes: manual, and negotiate.
In either case, the key returned will be a long. If you need a string,
the struct library, Crypto.Util.number.long_to_bytes(), or a hashing algorithm
will get the job done.

In manual mode you will call the update() and getPublicKey() functions.
Transmission will be entirely your resposibility. This allows you to
have fine grain control over how the traffic is managed, how the
sockets are configured, alternative transfer methods (UDP, files, IPC,
or other), etc. 

A local example of manual mode requiring no sockets is as follows:
```python
    >>> import DHE
    >>>
    >>> Alice = DHE.new()
    >>> Bob = DHE.new()
    >>>
    >>> aliceFinal = Alice.update(Bob.getPublicKey())
    >>> bobFinal = Bob.update(Alice.getPublicKey())
    >>>
    >>> (aliceFinal == bobFinal)
    True
```

As you can see, each instance must call update(), passing in the other's
public key. How you send that public key is up to you. That's why I call it 
manual mode. You need only do Alice (or Bob, its just a name), because the
other side is the remote end, and is only shown for demonstration.

For most appications, manual isn't nessesary. We have negotiate():
```python
    >>> import socket
    >>> import DHE
    >>>
    >>> sock = socket.socket()
    >>> sock.connect(('localhost', 1234))
    >>>
    >>> alice = DHE.new(18)
    >>> key = alice.negotiate(sock)
```

This is really easy. 
1. create a new, blocking, tcp socket and get it connected.
2. call x = DHE.new() with the desired group.
3. Call x.negotiate(sock)
4. Done! this socket may be closed, or you can use it for any other purpose.

other usage notes:
- update() will return the final key, but if you happen to miss it, or need
it again, you can call getFinalKey()
- update() can be called multiple times. This allows you to create multi-party
keys. This is not tested currently, use at your own risk.


## Inclusion in other Projects

I intend to submit pull requests for other libraries and projects likely
pyCrypto, pyCryptodome, pyca/cryptography, and others, but I am also making
this into a standalone module because it is easier to maintain, and under my
control. I cannot guarantee that those pull requests will be accepted or
maintained well, so at least my code will always live here.

## Contributing

I love contributions! The more the merrier. Please submit pull requests all
day long! I only ask that any changes you make be pep8 compliant and
accompanied by unit tests.

## Disclaimer

I am not a world renowned cryptographer. I know the saying goes "never roll
your own crypto" but it doesn't seem like anybody else will write this. I am
quite sure I cannot cover every facet, and there is probably a timing oracle,
parameter injection, birthday attack, or something in here. (Its not written
in C, so I can nearly guarantee there is a timing oracle at least.) It should
be good enough for most things, but if you are the NSA, or an enemy of the
NSA, maybe you should find a different library.

## License

Because crypto is important and everyone should access to strong crypto, I am
releasing this project under an extremely open license, the BSD 2-clause
license. This is uncharacteristic of me, because I usually opt for the GPLv3,
BUT this license will ensure that this project will be usable anywhere! Please,
spread it like the plague. Make sure everyone has easy access to DH.

## Footnotes

1. You must use the same group (i.e. DHE.new(x) ) on both ends, or else you
end up with non matching keys. If omited, the default group is 14.

2. negotiate() currently only supports newly created, never used, blocking,
TCP sockets. Support for nonblocking and UDP sockets may come eventually.
You can use previously used sockets, BUT I do not condone it, as anything
left in the network buffer will interfere and corrupt the key.
