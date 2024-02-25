from pprint import pprint

from jwcrypto.jwk import JWK
from jwt import JWT, jwk_from_dict

jwt = JWT()


def generate_keys():
    jwk = JWK.generate(kty="RSA", size=2048, alg="RS256", use="sig", kid="420")
    return jwk.export_private(as_dict=True), jwk.export_public(as_dict=True)


def encode(data, key):
    jwk = jwk_from_dict(key)
    return jwt.encode(data, jwk, alg="RS256", optional_headers={"typ": "JWT"})


def decode(token, key):
    jwk = jwk_from_dict(key)
    return jwt.decode(token, jwk)


if __name__ == "__main__":
    data = {
        "sub": "1234567890",
        "name": "John Doe",
        "admin": True,
        "iat": 1516239022,
        "exp": 100,
    }

    private_key, public_key = generate_keys()
    token = encode(data, private_key)
    payload = decode(token, public_key)
    print(payload == data)
