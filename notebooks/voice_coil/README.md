# Bl, a loudspeaker's force factor

Notebook and code by Claude, 2026-10-25. Capture is doc's proposed name, posited.

Bl is the field in a speaker's magnet gap times the length of wire in it. It's the push
per amp and the voltage per speed, because it's the flux the coil captures per meter it
moves. Capture is the same thing per radian of turning.

```sh
git pull
conda activate dog-math
cd notebooks/voice_coil
jupyter lab Claude-Voice-Coil-2610251406.ipynb
```

The saved notebook shows its pictures and numbers without a kernel; the panel at the end
needs one. Same environment as `../coiled_ring` (its `requirements.txt`).

- `speaker.py`: the speaker's numbers, and what Bl is and does
- `tap.py`: the cone ringing down after a tap
- `view.py`: the motor cut in half, and the ringdown, drawn with Manim
- `panel.py`: sliders for the field and windings, and what's across the leads
- `test_speaker.py`: Bl checked from both sides, and the tap's energy all ending as heat
- `make_notebook.py`: rebuilds and runs the notebook

```sh
python -m pytest -q
```
