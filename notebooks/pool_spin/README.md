# A spinning ball can't give its spin away

Notebook and code by Claude, 2026-10-26.

A sidespun pool ball hits a still one, seen from above. Along the line of centers the
balls push and trade travel; across it their faces skid, and friction is the only way
spin passes. Pool balls are slick, so the spin stays home.

```sh
git pull
conda activate dog-math
cd notebooks/pool_spin
jupyter lab Claude-Pool-Spin-2610261000.ipynb
```

The saved notebook shows its pictures and numbers without a kernel; the panel at the end
needs one. Same environment as `../coiled_ring` (its `requirements.txt`).

- `hit.py`: the balls, the shot, and the instant of the hit
- `view.py`: the hit and where the thump goes, drawn with Manim
- `panel.py`: sliders for the travel, the sidespin, the hit's fullness, the face friction, and the bounce
- `test_hit.py`: motion and spin kept, heat as friction over the skid, and the throw's direction
- `make_notebook.py`: rebuilds and runs the notebook

```sh
python -m pytest -q
```
