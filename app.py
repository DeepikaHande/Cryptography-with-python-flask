from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
from random import choice
import string


def convert_to_string(byte):
    i = 0
    a = []
    c = ""
    while i < len(byte):
        a.append(byte[i:i + 7])
        i += 7
    for i in a:
        c += chr(int(i, 2))
    return c


def gen_random_key(n):
    """Generates a random key of bits (with 0s or 1s) of length n"""
    k = []
    for i in range(n):
        k.append(choice(["0", "1"]))
    return "".join(k)


def xor(m, k):
    r = []
    for i, j in zip(m, k):
        r.append(str(int(i) ^ int(j)))  # xor between bits i and j
    return "".join(r)


@app.route('/')
def encryption():
    l = []
    str1 = request.args.get('plain_txt')
    l = str1.split(" ")
    for i in l:
        s = "".join(l)
        bits = "".join(format(ord(x), 'b') for x in s)
        key = gen_random_key(len(bits))
        cipher = xor(bits, key)
        plain_text=decryption(cipher, key)

    # print(cipher)
    cipher_txt = convert_to_string(cipher)
    # print(cipher_txt)
    return render_template('first.html', txt_ct=cipher_txt,d_txt=plain_text)

# encryption()[1]
@app.route('/')
def decryption(cipher, key):
    plain = xor(cipher, key)
    plain_txt = convert_to_string(plain)
    return plain_txt


if __name__ == '__main__':
    app.run(debug = True)
