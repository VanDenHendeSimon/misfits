import random
import math


PRIME = 23
GENERATOR = 11


def validate_key(my_private_key, other_party_public_key):
    return (math.pow(other_party_public_key, my_private_key)) % PRIME


def get_public_key(private_key):
    return (math.pow(GENERATOR, private_key)) % PRIME


def main():
    private_key_a = random.randrange(1, GENERATOR)
    private_key_b = random.randrange(1, GENERATOR)
    print("A chose its private key: %s" % private_key_a)
    print("B also chose its private key, but no one knows it except for B\n")

    public_key_a = get_public_key(private_key_a)
    public_key_b = get_public_key(private_key_b)
    print("A has turned its private key into a public key (%s), which will be sent to B" % public_key_a)
    print("B has also turned its private key into a public key and has sent it to A: %s" % public_key_b)
    print("The formula to turn a private key into a public key is: (math.pow(GENERATOR, private_key)) % PRIME\n")

    shared_code = validate_key(private_key_a, public_key_b)
    print("Using B's public key, A was able to compute the shared code (%s)" % shared_code)
    print("The formula to turn a public key into a shared secret is: (math.pow(other_party_public_key, my_private_key)) % PRIME\n")

    if validate_key(private_key_a, public_key_b) == validate_key(private_key_b, public_key_a):
        print("Codes are the same across both parties")
    else:
        print("Codes do not match")


if __name__ == '__main__':
    main()
