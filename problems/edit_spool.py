import subprocess
st = subprocess.run(['bash', '-c', 'TZ=America/New_York date "+%y%m%d%H%M"'], capture_output=True, text=True).stdout.strip()
src = '/home/claude/out/Claude The Spool That Wont Roll 2610191306.txt'
s = open(src, encoding='utf-8').read()
R = [
 ('Written by Claude (Anthropic), 2026-10-19 13:06.', 'Written by Claude (Anthropic), 2026-10-19 %s:%s.' % (st[6:8], st[8:])),
 ('''member; cosine is how many forwards a direction is worth, theta
over forward.''', '''member; dividing anything by a direction counts how many of that
direction it is worth.'''),
 ('''The lever from the centre
down to the floor line is 2 hands; measured in string-normals it
is worth 2 hands times the cosine of the string's angle. The axle
takes 1 hand of that back:

        offset = 2 hands (cosine of the pull angle) - 1 hand.''', '''The lever from the centre
down to the floor line is 2 hands. Count how many string-normals
it is worth, and the axle takes 1 hand of that back:

        offset = (2 hands down) / string-normal - 1 hand.'''),
 ('''A shallow pull: the cosine is near one, the offset is near
+1 hand, and the string's leverage turns the spool toward you.''', '''A shallow pull: the string-normal points nearly straight down,
the 2-hand lever is worth nearly 2 hands of it, the offset is near
+1 hand, and the string's leverage turns the spool toward you.'''),
 ('''A steep pull: straight up, the cosine is nothing and the offset is
-1 hand.''', '''A steep pull: straight up, the string-normal points straight
across, the lever is worth none of it, and the offset is -1 hand.'''),
 ('''The offset is zero when the cosine is 1 hand over 2 hands:

        the string's direction is worth half a forward.

Half a forward is a sixth of a turn up from the floor. No trig was
solved; the angle came out as a ratio. In general, (c):

        the string's direction is worth r over R of a forward.''', '''The offset is zero when the 2-hand lever is worth exactly 1 hand
of string-normal: when down is worth half a string-normal. The
string is square to its normal, as forward is square to down, so
the same count says the string is worth half a forward.

Half a forward is a sixth of a turn up from the floor. No trig was
solved; the angle came out as a ratio. In general, (c):

        the string's direction is worth r over R of a forward.'''),
 ('''The lever is 2 hands down. Measured in string-normals, it is
worth 2 hands times the cosine: a length, so it can take the
axle's 1 hand away.''', '''The lever is 2 hands down. Counted in string-normals, it comes
out in hands: a length, so it can take the axle's 1 hand away.'''),
 ('''        offset = R cos theta - r
        leverage about the floor line = F (R cos theta - r)
        no motion when cos theta = r / R''', '''With n the string-normal:

        offset = (R down) / n - r
        leverage about the floor line = F ((R down) / n - r)
        no motion when down / n = r / R

(down / n is what the textbook writes cos theta.)'''),
 ('''  - Reading the cosine as how many forwards the string is worth
    made the special angle a ratio of radii, with no inverse trig.''', '''  - Counting the lever in string-normals made the special angle a
    ratio of radii, with no trig function written and none
    inverted.'''),
]
for a, b in R:
    assert a in s, a[:60]
    s = s.replace(a, b)
out = '/home/claude/out/Claude The Spool That Wont Roll %s.txt' % st
open(out, 'w', encoding='utf-8').write(s)
print(out, max(len(l) for l in s.splitlines()), s.lower().count('cos'))
