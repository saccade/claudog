import subprocess
st = subprocess.run(['bash', '-c', 'TZ=America/New_York date "+%y%m%d%H%M"'], capture_output=True, text=True).stdout.strip()
src = '/home/claude/out/Claude The Bulk Swings 2610191244.txt'
s = open(src, encoding='utf-8').read()
R = [
 ('Written by Claude (Anthropic), 2026-10-19 12:44.', 'Written by Claude (Anthropic), 2026-10-19 %s:%s.' % (st[6:8], st[8:])),
 ('''Uses the 12:27 glossary: a card is a square hand; profile is
inertia per mass; zing is hook per inertia; cosine and sine are
the part over the whole.''', '''Uses the 13:02 glossary: a card is a square hand; profile is
inertia per mass; zing is hook per inertia; cosine and sine are
what fraction of a direction's forward and up it is.'''),
 ('''Measure the swing from straight down. A sixth of a turn out, the
rod's direction is partly down and partly across. The across part,
over the whole, is the sine of a sixth of a turn: a little under
nine tenths.''', '''Measure the swing from straight down. A sixth of a turn out, the
rod's direction is worth a little under nine tenths of an across:
divide the direction by across and that is what you count. It is
the sine of a sixth of a turn.'''),
 ('''A sixth of a turn out, the down part of the rod's direction, over
the whole, is the cosine: one half. So every bit of the pendulum
sits half as far below the pivot as it will at the bottom, and the
bulk has a half-reach still to fall.

The heft it gives up is the bulk under gravitation over that half:

        0.8 ponder under 10 zoom, times 1/2 = 4 thump.''', '''The heft of the bulk is the bulk under gravitation, as many ups
as the rod's direction is worth:

        heft = g β (θ / ↑),  also g β (↑ · θ).

The upwardness is what it physically is, and the dot is what it
mathematically is; the fraction says it more usefully. Straight
down, the rod's direction is worth minus one up. A sixth of a turn
out it is worth minus one half: it is half a down. So the bulk
sits half a reach higher than at the bottom, and that half is
what it has still to fall:

        0.8 ponder under 10 zoom, times 1/2 = 4 thump.'''),
 ('''Check the endpoints: let it go straight down and the cosine is
one, nothing falls, and there is no hook. Let it go from level and
the cosine is nothing, the bulk's whole reach (4 hands, the bulk
over the mass) falls, and the hook doubles to 8 thump.''', '''Check the endpoints: let it go straight down and the rod is worth
a whole down, nothing falls, and there is no hook. Let it go from
level and it is worth no down at all, the bulk's whole reach (4
hands, the bulk over the mass) falls, and the hook doubles to 8
thump.'''),
 ('''  - The sine and cosine are each read as a part over the whole,
    so each one says what it is doing: the across part gives the
    leverage, the down part gives the fall.''', '''  - The sine and cosine are each read as what fraction of across
    or up the rod's direction is worth, so each one says what it
    is doing: the across fraction gives the leverage, the up
    fraction gives the heft.'''),
]
for a, b in R:
    assert a in s, a[:60]
    s = s.replace(a, b)
out = '/home/claude/out/Claude The Bulk Swings %s.txt' % st
open(out, 'w', encoding='utf-8').write(s)
print(out, max(len(l) for l in s.splitlines()))
