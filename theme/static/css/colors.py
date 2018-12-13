#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import math
import struct
import skimage.color as skcolor
import jinja2

def _hex2rgb(s):
   '''s is 6-character string for standard hex colors (no `#`)'''
   return struct.unpack('BBB', bytes.fromhex(s))

def _rgb2hex(rgb):
   '''rgb is list [r, g, b]'''
   return bytes.hex(struct.pack('BBB', *rgb))

def _hex2lab(s):
   '''s is 6-character string for standard hex colors (no `#`)'''
   return skcolor.rgb2lab([[[x / 255 for x in _hex2rgb(s)]]])[0][0]

def _lab2hex(lab):
   '''lab is list [l, a, b]'''
   return _rgb2hex([int(x) for x in (skcolor.lab2rgb([[lab]])[0][0] * 255)])

def _hexable(lab):
   '''lab is valid hex value'''
   new_lab = _hex2lab(_lab2hex(lab))
   val = sum([(new_lab[i] - lab[i]) ** 2 for i in [0, 1, 2]]) < 1
   return val

def _saturate(lab):
   '''
   get maximum saturated lab values at this l, along the same radius
   in the ab plane
   '''
   l, a, b = lab

   phi = math.atan2(b, a)

   test = [
      l,
      127 * math.sqrt(2) * math.cos(phi),
      127 * math.sqrt(2) * math.sin(phi)
   ]

   # binary search
   for i in range(13):
      if _hexable(test):
         test[1] += test[1] / 2
         test[2] += test[2] / 2
      else:
         test[1] -= test[1] / 2
         test[2] -= test[2] / 2

   return test

###############################################################################

# TMZ - yet another parameterization of color:
# (scaling of CIELAB space in cylindrical coords, but using manhattan distance,
#  so not actually a cylinder)
# T - theta, M - Manhattan distance, Z - 3rd dimension
#
#                 point in question
#
# Yellow    1|     0 <-boundary point (maximally saturated color
#            |                           resolvable to hex at this T, Z)
#         B >|--0 <- point of interest
#            | /
#            |/)<-T              Let l, a, b be coordinates in CIELAB
# -----------+-----------        and T, M, Z be coordinates in TMZ
# -1         |  ^       1        l is in [0, 100]; a and b are in [-127, 127]
#            |  A
#            |                   We have A = a / 127; B = b / 127
# Blue       |                   # T = arctan2(B, A)           [-pi, pi]
#   Green  -1|          Red      # M = (abs(A) + abs(B)) / 2      [0, 1]
###########################      # Z = l / 100.                   [0, 1]

def _hex2tmz(s):
   l, a, b = _hex2lab(s)
   t = math.atan2(b, a)
   m = (abs(a) + abs(b)) / 255.
   z = l / 100.

   return t, m, z

def _tmz2hex(tmz):
   '''tmz as [t, m, z]'''
   t, m, z = tmz

   c = math.cos(t)
   s = math.sin(t)

   bnd_lab = _saturate([z * 100., c, s])
   bnd_m = (abs(bnd_lab[1]) + abs(bnd_lab[2])) / 255.

   r = 2 * min(m, bnd_m) / (abs(c) + abs(s))

   return _lab2hex([z * 100., c * r * 127., s * r * 127.])


# public methods on hex colors which make reference to CIELAB/TMZ space
##############################################################################

def rotate(s, deg):
   '''
   rotate hue while preserving luminosity by angle in CIELAB's (a, b) plane
   '''
   t, m, z = _hex2tmz(s)
   t += deg / 180 * math.pi
   return _tmz2hex([t, m, z])

def reflect(s, axis_angle):
   '''
   reflect hue about an axis in ab plane
   '''
   t, m, z = _hex2tmz(s)
   t = (2 * axis_angle) - t
   return _tmz2hex([t, m, z])

def project(s, axis_angle):
   '''
   project color along a line with angle `axis_angle` in (a, b) plane
   '''
   t, m, z = _hex2tmz(s)
   m = m * math.cos(t - axis_angle)
   t = axis_angle
   return _tmz2hex([t, m, z])

def grey(s):
   '''
   eliminate color information (project to origin in (a, b) plane)
   '''
   t, m, z = _hex2tmz(s)
   m = 0
   return _tmz2hex([t, m, z])

def invert_luma(s):
   '''
   invert luminosity
   '''
   t, m, z= _hex2tmz(s)
   return _tmz2hex([t, m, 1. - z])

# Compositions must be peformed together, or we might lose saturation
# at an intermediate step

def invert_rotate(s, deg):
   '''
   rotate hue while preserving luminosity by angle in CIELAB's (a, b) plane
   '''
   t, m, z = _hex2tmz(s)
   t += deg / 180 * math.pi
   return _tmz2hex([t, m, 1. - z])

def invert_reflect(s, axis_angle):
   '''
   reflect hue about an axis
   '''
   t, m, z = _hex2tmz(s)
   t = (2 * axis_angle) - t
   return _tmz2hex([t, m, 1. - z])

def invert_project(s, axis_angle):
   '''
   project color along a line with angle `axis_angle` in (a, b) plane
   '''
   t, m, z = _hex2tmz(s)
   m = m * math.cos(t - axis_angle)
   t = axis_angle
   return _tmz2hex([t, m, 1. - z])

###############################################################################

# https://github.com/nashamri/spacemacs-theme/blob/master/spacemacs-common.el
# http://www.workwithcolor.com/color-converter-01.htm

variables = {

    # whites (by brightness)
    "w2": "#cccccc",
    "w1": "#bababa",
    "w0": "#b2b2b2",

    # greys (by darkness)
    "g4": "#191919",
    "g3": "#222222",
    "g2": "#272727",
    "g1": "#2e2e2e",
    "g0": "#3b3b3b",

    # primary color sequence
    "h1": "#4f97d7",  # h1 (blue)
    "h2": "#2d9574",  # h2 (blue-green)
    "h3": "#67b11d",  # h3 (yellow)
    "h4": "#b1951d",  # h4 (orange)

    # subtle colors
    "s1": "#a2b2d2",  # blockquote color
    "s2":  "#409b9b",  # link (teal)

    # loud colors
    "e1": "#df5e8c",  # emphasis (pink)

    # unused spacemacs colors
    "sm_str":     "#2d9574",  # green
    "sm_comment": "#2aa1ae",  # teal
    "sm_const":   "#a45bad",  # purple
    "sm_cursor":  "#b1951d",  # yellow
    "sm_func":    "#bc6ec5",  # pinkish

    # Syntax highlighting (pygments)
    "hl_err_c":      "#960050",  # Error
    "hl_err_bg":     "#1e0010",  # Error background
    "hl_hll":        "#49483e",  # Highlight ?
    "hl_bg":         "#272822",  # Default Background
    "hl_cl":         "#f8f8f2",  # Default Color
    "hl_c":          "#75715e",  # Comment
    "hl_k":          "#66d9ef",  # Keyword
    "hl_l":          "#ae81ff",  # Literal
    "hl_n":          "#f8f8f2",  # Name
    "hl_o":          "#f92672",  # Operator
    "hl_p":          "#f8f8f2",  # Punctuation
    "hl_ch":         "#75715e",  # Comment.Hashbang
    "hl_cm":         "#75715e",  # Comment.Multiline
    "hl_cp":         "#75715e",  # Comment.Preproc
    "hl_cpf":        "#75715e",  # Comment.PreprocFile
    "hl_c1":         "#75715e",  # Comment.Single
    "hl_cs":         "#75715e",  # Comment.Special
    "hl_gd":         "#f92672",  # Generic.Deleted
    "hl_gi":         "#a6e22e",  # Generic.Inserted
    "hl_gu":         "#75715e",  # Generic.Subheading
    "hl_kc":         "#66d9ef",  # Keyword.Constant
    "hl_kd":         "#66d9ef",  # Keyword.Declaration
    "hl_kn":         "#f92672",  # Keyword.Namespace
    "hl_kp":         "#66d9ef",  # Keyword.Pseudo
    "hl_kr":         "#66d9ef",  # Keyword.Reserved
    "hl_kt":         "#66d9ef",  # Keyword.Type
    "hl_ld":         "#e6db74",  # Literal.Date
    "hl_m":          "#ae81ff",  # Literal.Number
    "hl_s":          "#e6db74",  # Literal.String
    "hl_na":         "#a6e22e",  # Name.Attribute
    "hl_nb":         "#f8f8f2",  # Name.Builtin
    "hl_nc":         "#a6e22e",  # Name.Class
    "hl_no":         "#66d9ef",  # Name.Constant
    "hl_nd":         "#a6e22e",  # Name.Decorator
    "hl_ni":         "#f8f8f2",  # Name.Entity
    "hl_ne":         "#a6e22e",  # Name.Exception
    "hl_nf":         "#a6e22e",  # Name.Function
    "hl_nl":         "#f8f8f2",  # Name.Label
    "hl_nn":         "#f8f8f2",  # Name.Namespace
    "hl_nx":         "#a6e22e",  # Name.Other
    "hl_py":         "#f8f8f2",  # Name.Property
    "hl_nt":         "#f92672",  # Name.Tag
    "hl_nv":         "#f8f8f2",  # Name.Variable
    "hl_ow":         "#f92672",  # Operator.Word
    "hl_w":          "#f8f8f2",  # Text.Whitespace
    "hl_mb":         "#ae81ff",  # Literal.Number.Bin
    "hl_mf":         "#ae81ff",  # Literal.Number.Float
    "hl_mh":         "#ae81ff",  # Literal.Number.Hex
    "hl_mi":         "#ae81ff",  # Literal.Number.Integer
    "hl_mo":         "#ae81ff",  # Literal.Number.Oct
    "hl_sa":         "#e6db74",  # Literal.String.Affix
    "hl_sb":         "#e6db74",  # Literal.String.Backtick
    "hl_sc":         "#e6db74",  # Literal.String.Char
    "hl_dl":         "#e6db74",  # Literal.String.Delimiter
    "hl_sd":         "#e6db74",  # Literal.String.Doc
    "hl_s2":         "#e6db74",  # Literal.String.Double
    "hl_se":         "#ae81ff",  # Literal.String.Escape
    "hl_sh":         "#e6db74",  # Literal.String.Heredoc
    "hl_si":         "#e6db74",  # Literal.String.Interpol
    "hl_sx":         "#e6db74",  # Literal.String.Other
    "hl_sr":         "#e6db74",  # Literal.String.Regex
    "hl_s1":         "#e6db74",  # Literal.String.Single
    "hl_ss":         "#e6db74",  # Literal.String.Symbol
    "hl_bp":         "#f8f8f2",  # Name.Builtin.Pseudo
    "hl_fm":         "#a6e22e",  # Name.Function.Magic
    "hl_vc":         "#f8f8f2",  # Name.Variable.Class
    "hl_vg":         "#f8f8f2",  # Name.Variable.Global
    "hl_vi":         "#f8f8f2",  # Name.Variable.Instance
    "hl_vm":         "#f8f8f2",  # Name.Variable.Magic
    "hl_il":         "#ae81ff"   # Literal.Number.Integer.Long
}


def write_with_func(name, func):
    print('writing', name + '.css')

    with open(name + '.css', 'w') as f:

        with open('color.css.template') as t:
            x = jinja2.Template(t.read())

        f.write(
            x.render(**{
                k: '#' + func(v[1:]) \
                for k, v in variables.items() \
            })
        )

if __name__ == '__main__':
    write_with_func(
        'color-dark-default', lambda x: x
    )
    write_with_func(
        'color-dark-rotated', lambda x: rotate(x, 90)
    )
    write_with_func(
        'color-light-default', lambda x: invert_luma(x)
    )
    write_with_func(
        'color-light-rotated', lambda x: invert_rotate(x, 90)
    )
