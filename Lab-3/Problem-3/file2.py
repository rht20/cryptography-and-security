#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           �*\�z2��k��@��ia�שo���AU�����L�o�g�[:.R��#�'6/qn�"�Va�C������S�4��1�'f&��n���iV����K��na�^ly�4�&rcv�pf�d��b�
"""
from hashlib import sha256
print sha256(blob).hexdigest()

sha = "2765d27f9776858c5a64084545b88e2f0387564e25492b624b4f46a79728cda2"
if sha256(blob).hexdigest() == sha:
    print("I come in peace.")
else:
    print("Prepare to be destroyed!")
