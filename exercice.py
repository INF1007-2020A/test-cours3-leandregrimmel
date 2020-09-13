#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    mot_output = ''
    for lettre in mot:
        lettre = ord(lettre) - 32
        mot_output += chr(lettre)
    return mot_output


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre',
        'yolo'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
