"""Different attention along the four routes, from the workbook's Clowns table.
Codex (OpenAI), 2026-10-23, for dr. kraemer. Model working prose.
Keep the common clues and mechanical joins; no clowns enter the lower levels.
The choices are deliberately uneven. A room need not supply a new observation
to every route. Nothing in the ending or final chorus is replaced.
"""

CURTSY = "At the silver pivot, a powdered clown in damask is partway into a curtsy."
STEAM = "Ahead, something breathes in steam."
LIBRARY = "On the reading table, a velvet kit,"
CHALK = "The chalk is on your cuff."
BASIN = "Its own height pays for its motion."
BALLROOM = "Their cycles keep time; their starting positions are still theirs to choose."
SLEEVE = "Someone took that sleeve in, and wore it."
HALL = "The hall asks what could announce the release."
THUMBS = "The silk at the shoulders has faded round two small thumbprints."

# Replacements keep their anchor, so the known clue/transition remains visible.
ENTRY = {
    1: [
        (CURTSY, CURTSY + " The small ruff is folded like a starched napkin; a gravy-brown tear marks the white cheek."),
        (LIBRARY, "Half-moon spectacles sit on the crazed white face. A spider has the whiskey glass to itself. " + LIBRARY),
        (CHALK, CHALK + " The clown’s worsted has been pressed so stiff that one crease stands clear of the leg."),
        (BASIN, BASIN + " The clown’s damp hem smells of rain just beginning; the collar, of rain that stopped yesterday."),
        (BALLROOM, BALLROOM + " In the mirror, the clown wears a brooch of mirror glass. It holds a smaller room."),
    ],
    2: [
        (CURTSY, CURTSY + " The visitor studies the curtsy: spine upright, knees flexed, rear toe crossed behind. It ought to be over by now."),
        (CHALK, CHALK + " Each horn button has a worn spot, two fifths of its radius above its middle."),
        (BALLROOM, BALLROOM + " In the mirror, a hoop bangle turns round the clown’s wrist. The visitor watches the contact: each part is still when it touches the skin."),
        (SLEEVE, SLEEVE + " The amber mending is translucent. The lining under it doesn’t match the collar."),
        (THUMBS, THUMBS + " The gown is flattened across the back, keeping the shape of someone sitting. The clown is standing."),
    ],
    3: [
        (CURTSY, CURTSY + " Inside one starched cuff is another, its button fastened."),
        (STEAM, STEAM + " The leather at the clown’s elbow shines on the side that doesn’t bend. The shaft keeps going."),
        (LIBRARY, "With the nap, black; against it, bottle-green. The clown hasn’t turned. " + LIBRARY),
        (CHALK, CHALK + " At the clown’s heel, the wool has twisted into a hard little cord."),
        (BALLROOM, BALLROOM + " In the mirror, one heel has the hem pinned. Enough slack for the next step. No more."),
    ],
    4: [
        (CURTSY, CURTSY + " Two earrings hang one from the other. The knife comes home; the earrings don’t."),
        (LIBRARY, "One brace hangs loose. Two thirds down, the shoulder let it go. " + LIBRARY),
        (CHALK, CHALK + " Shoulders square. Hips square. The shot seems to be lined up on you."),
        (BALLROOM, BALLROOM + " In the mirror, one fold says forward; the next says back. The taffeta was cut both ways."),
    ],
}

# These observations land after a physical result, not at every doorway.
AFTER = {
    2: {
        "3-d": "The visitor follows a thread from the clown’s cuff, low along the floor, to a cotton reel.",
    },
    3: {
        "11-c": "The hall clown’s shoulders are close to the cornice. The lining stops; the coat goes on.",
    },
    4: {
        "6-a": "The clown has a bell at one wrist, a bead in the other palm. The bead takes the shorter road. They keep time.",
        "11-c": "Stripes run up the clown’s stockings. Not a stitch goes with them.",
        "12-c": "One eye is four times as bright as the other. Lean the right way and they match.",
    },
}

def apply(items, path):
    out = list(items)
    for old, new in ENTRY.get(path, []):
        count = sum(s.count(old) for _, s in out if isinstance(s, str))
        assert count == 1, ("clown observation anchor changed", path, old, count)
        out = [(t, s.replace(old, new) if isinstance(s, str) else s) for t, s in out]
    for label, observation in AFTER.get(path, {}).items():
        hits = [i for i, (t, s) in enumerate(out) if t == "p" and s.startswith(f"({label})")]
        assert len(hits) == 1, ("clown observation part changed", path, label, len(hits))
        out.insert(hits[0] + 1, ("i", observation))
    return out
