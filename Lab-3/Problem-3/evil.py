#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           �*\�z2��k��@��ia�שo���AU�����L�o�g�[:.R��#�'6/qn�"�Va�C������S�4��1�'f&��n���iV����K��na�^ly�4�&rcv�pf�d��b�
"""
from hashlib import sha256
print sha256(blob).hexdigest()

sha = "0991bdc5abb31d96340fe346023cd0061f7a804e4ccc28a619a99517190d17f4"
if sha256(blob).hexdigest() == sha:
    print("I come in peace.")
else:
    print("Prepare to be destroyed!")
