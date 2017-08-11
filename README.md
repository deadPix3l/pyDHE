# pyDHE

pyDHE is a simple to use Diffie-Hellman implementation written in python, for
python. It makes using Diffie-Hellman a breeze so you can focus on the real
crypto. Eventually, I hope to include elliptic curves (ECDHE) but that is not
currently supported.

## why?

For several of my other projects, I've needed a Diffie-Hellman-Ephemeral (DHE)
implementation, but could never find one. The algorithm is not hard, but I was
always surprised when I searched for a prewritten one, and never found it.
Even well known Crypto libraries like pyCrypto, pyCryptodome, and cryptography
lacked Diffie-Hellman. So I always write my own. Eventually I decided to make
that terrible code i used previously and generalize it. Make it easy, readable,
pep8 and pep257 compliant, write unit tests and release it to the world!

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
