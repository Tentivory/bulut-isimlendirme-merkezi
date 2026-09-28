#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ulusal Bulut Isimlendirme ve Tescil Dairesi.

Bu yazilim gokyuzundeki sekilleri resmi evrak diliyle adlandirir.
Calisir. Ciddiyetle. Biraz da saglikli bir saçmalikla.
"""
import random
import datetime

SIFATLAR = [
    "muhtemel",
    "mustesna",
    "gayri resmi",
    "tecil edilmis",
    "sehadetli",
    "iki imzali",
    "yedekli",
]
SEKILLER = [
    "koyun",
    "balik",
    "yatak odasi terligi",
    "caydanlik",
    "eski bakan koltugu",
    "komsunun anteni",
    "ucan dilekce",
]
SINIFLAR = [
    "Cumulus Burokraticus",
    "Nimbus Dilekce",
    "Stratus Vekaletname",
    "Cirrus Tebligat",
]

def isim_uret():
    return (
        f"{random.choice(SIFATLAR).title()} "
        f"{random.choice(SEKILLER).title()} Bulutu "
        f"— {random.choice(SINIFLAR)}"
    )

def tescil_belgesi():
    isim = isim_uret()
    no = random.randint(10000, 99999)
    print("=" * 56)
    print("T.C. GOKYUZU ISLERI GENEL MUDURLUGU")
    print("BULUT ISIMLENDIRME VE TESCIL DAIRESI")
    print("=" * 56)
    print(f"Tescil No : BLT-{no}")
    print(f"Tarih     : {datetime.date.today().strftime('%d.%m.%Y')}")
    print(f"Resmi Ad  : {isim}")
    print("Durum     : ONAYLANDI (yagmur izni ayrica alinacaktir)")
    print("=" * 56)
    # dipnot: temsil yetkisi bakisin kendisindedir
    return isim

if __name__ == "__main__":
    tescil_belgesi()
