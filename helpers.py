import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps
from itertools import product
from math import floor, ceil


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

def gardnercal(m, n, k):
    mn = float(m * n)
    case = [ele for ele in product(range(0, m), repeat = k)]
    rs = []
    for i in case:
        pstart = 1.0
        pend = mn
        for j in range(1, k + 1):
            l = i[j - 1]
            pstart = ceil(pstart / m) + (l * n)
            pend = ceil(pend / m) + (l * n)
        if (pstart == pend):
            rs.append((int(pstart), int(pend), i))
    rs.sort()

    tposition = ['Position']
    tcode = ['Code']
    isfindall = True
    j = 1
    for i in range(1, int(mn) + 1):
        tposition.append(i)
        isfind = False
        listcode = []
        for j in range(j, len(rs) + 1):
            result_success = rs[j - 1]
            position = result_success[0]
            if (i != position):
                break
            isfind = True
            code = result_success[2]
            code = code[::-1]
            code = str(code).replace(', ','').replace('(','').replace(')','')
            listcode.append(code)
        if (isfind == False):
            isfindall = False
        tcode.append(listcode)
    if (isfindall == False):
        x = "Unsolvable"
    else:
        x = "Solvable"
    return x, tposition, tcode