# Power around a square

Notebook and code by Claude, 2026-10-26. Capture is doc's proposed name, posited.

A tractor's PTO turns machine 1; a belt carries the turning to machine 2, 5 to 3; machine 2's
wires run back to machine 1. Power goes around the square, and the tractor pays only for the
heat. One coil of machine 2 is worked out two ways: forces on its sides times levers you add
and then drop, and the flux it links as it turns.

```sh
git pull
conda activate dog-math
cd notebooks/power_square
jupyter lab Claude-Power-Square-2610261155.ipynb
```

The saved notebook shows its pictures and numbers without a kernel; the panel at the end
needs one. Same environment as `../coiled_ring` (its `requirements.txt`).

- `square.py`: the tractor, the belt, the two machines, and the power and torque at each corner
- `coil.py`: one coil in a leaning field, the lever way and the capture way
- `view.py`: the square's power flows, and the coil's linkage and torque, drawn with Manim
- `panel.py`: sliders for machine 2's capture, the tractor's sweep, and the windings
- `test_square.py`: the tractor pays only for heat, each shaft holds steady, both ways agree
- `make_notebook.py`: rebuilds and runs the notebook

```sh
python -m pytest -q
```
