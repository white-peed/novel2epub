#!/usr/bin/env python3

# Copyright (C) 2017 GatoLoko
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

volumes = {'1': Volume('1', 1, 100),
           '2': Volume('2', 101, 200),
           '3': Volume('3', 201, 300),
           '4': Volume('4', 301, 400),
           '5': Volume('5', 401, 500),
           '6': Volume('6', 501, 600),
           '7': Volume('7', 601, 659),
           }

origin = 'http://www.wuxiaworld.co/My-Wife-is-a-Beautiful-CEO/'
author = 'Cabbage Flatbread (霉干菜烧饼)'
cover_file = 'Covers/My-Wife-is-a-Beautiful-CEO.jpg'
title = 'My wife is a beautiful CEO - Vol'

synopsis_text = """
This story takes place in Modern China. However, no matter how much things
change, in the depths of society, a secret world of syndicates and hidden
factions exist.</p>

<p>Yang Chen, a graduate from Harvard who is fluent in English, French,
Italian, and German to list a few. He is also capable of fighting and a number
of practical skills. Yet he chose to go on the streets to sell fried mutton
skewers for a living.</p>

<p>Lin Ruoxi is the CEO of a multibillion-dollar company—Yu Lei International.
This company is one of the leaders in the cosmetic and fashion industry.
Despite being only 20 years old, her ice-cold demeanor and beauty are
well-known and unrivaled in Zhonghai City.</p>

<p>Due to a wild night consisting of a lot of liquor, fate has brought them
together to become husband and wife.</p>

<p>And with that, the story begins!
"""

# Regex's for cleanup
volareline = re.compile(r'.*(volaretranslations)|(volarenovel).*')


def genlist(start, end):
    global origin
    list_page = common.get_html(origin)
    chapterlist = []
    for i in range(start, end+1):
        # print(i)
        text = '^Chapter %s: .*' % str(i)
        if i == 123:
            text = '^Chapter %s-1' % str(i)
            link = list_page.find('a', text=re.compile(text))
            url = origin + link['href']
            chapterlist.append(url)
            text = '^Chapter %s-2:' % str(i)
        elif i in range(124, 229+1) or i in [233, 253]:
            text = '^Chapter %s-1:.*' % str(i)
            link = list_page.find('a', text=re.compile(text))
            url = origin + link['href']
            chapterlist.append(url)
            text = '^Chapter %s-2:.*' % str(i)
        elif i == 250 or i >= 563:
            text = '^Chapter %s' % str(i)
        link = list_page.find('a', text=re.compile(text))
        url = origin + link['href']
        chapterlist.append(url)
    return chapterlist


def clean(content):
    for i in content.find_all(text=volareline):
        i.replaceWith('')
    return content