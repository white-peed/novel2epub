#!/usr/bin/env python3

# Copyright (C) 2019 GatoLoko
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

"""
Created on 19/02/19

@author: GatoLoko
"""

from common import Volume
import common
import re

volumes = {'1': Volume('1', 0, 100),
           '2': Volume('2', 101, 200),
           '3': Volume('3', 201, 300),
           '4': Volume('4', 301, 400),
           '5': Volume('5', 401, 500),
           '6': Volume('6', 501, 600),
           '7': Volume('7', 601, 700),
           '8': Volume('8', 701, 800),
           '9': Volume('9', 801, 900),
           '10': Volume('10', 901, 924),
           #
           '11': Volume('11', 1001, 1001),
           # This novel ends in chapter 1027.
           }

origin = 'http://www.wuxiaworld.co/Great-Demon-King/'
author = 'Ni Cang Tian (逆蒼天)'
cover_file = 'Covers/great-demon-king.jpg'
title = 'Great Demon King - Vol'

synopsis_text = """
“If I don’t die… I swear I will act on all my evil thoughts..”</p>

<p>Not exactly everyone’s typical thought when they’re about to die. What will
a cowardly young man do when reincarnated with the evil powers to redefine his
destiny? Can the natural kindness of human nature triumph over evil? Will he
become the cold-blooded demon king of legend, or will he forge his own path and
rain down another kind of terror?
"""


def genlist(start, end):
    global origin
    list_page = common.get_html(origin)
    chapterlist = []
    for i in range(start, end+1):
        # print(i)
        if i == 0:
            text = '^prologue'
        elif i in [424, 593, 621, 760]:
            text = '^Chapter %s' % str(i)
        elif i == 860:
            text = '^GDK 860'
        elif i == 868:
            text = '^Chapter868'
        else:
            text = '^Chapter %s: .*' % str(i)
        link = list_page.find('a', text=re.compile(text))
        url = origin + link['href'].split("/")[-1]
        chapterlist.append(url)
    return chapterlist


def clean(content):
    return content
