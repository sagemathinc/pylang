# vim:fileencoding=utf-8
# License: BSD Copyright: 2016, Kovid Goyal <kovid at kovidgoyal.net>
from __python__ import hash_literals

from ast_types import AST_BlockStatement, is_node_type


def best_of(a):
    best = a[0]
    len_ = best.length
    for i in range(1, a.length):
        if a[i].length < len_:
            best = a[i]
            len_ = best.length
    return best


def make_num(num):
    str_ = num.toString(10)
    a = [str_.replace(RegExp(r"^0\."), ".").replace("e+", "e")]
    m = None

    if Math.floor(num) is num:
        if num >= 0:
            a.push(
                "0x" + num.toString(16).toLowerCase(),  # probably pointless
                "0" + num.toString(8))
        else:
            a.push(
                "-0x" +
                (-num).toString(16).toLowerCase(),  # probably pointless
                "-0" + (-num).toString(8))

        m = RegExp(r"^(.*?)(0+)$").exec(num)
        if m:
            a.push(m[1] + "e" + m[2].length)

    else:
        m = RegExp(r"^0?\.(0+)(.*)$").exec(num)
        if m:
            a.push(m[2] + "e-" + (m[1].length + m[2].length),
                   str_.substr(str_.indexOf(".")))

    return best_of(a)


def make_block(stmt, output):
    if is_node_type(stmt, AST_BlockStatement):
        stmt.print(output)
        return

    def print_statement():
        output.indent()
        stmt.print(output)
        output.newline()

    output.with_block(print_statement)


def create_doctring(docstrings):
    ans = []
    for ds in docstrings:
        ds = str.rstrip(ds.value)
        lines = []
        min_leading_whitespace = ''
        for line in ds.split(RegExp(r"$", "gm")):
            r = RegExp(r"^\s+").exec(line)
            leading_whitespace = ''
            if r:
                leading_whitespace = r[0].replace(RegExp(r"[\n\r]", "g"),
                                                  '') if r else ''
                line = line[r[0].length:]
            if not str.strip(line):
                lines.push(["", ""])
            else:
                leading_whitespace = leading_whitespace.replace(
                    RegExp(r"\t", "g"), '    ')
                if leading_whitespace and (not min_leading_whitespace
                                           or leading_whitespace.length <
                                           min_leading_whitespace.length):
                    min_leading_whitespace = leading_whitespace
                lines.push([leading_whitespace, line])
        for lw, l in lines:
            if min_leading_whitespace:
                lw = lw[min_leading_whitespace.length:]
            ans.push(lw + l)
        ans.push('')
    return str.rstrip(ans.join('\n'))
