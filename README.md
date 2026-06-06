# Push 2 Pad Sensitivity Fix for Ableton Live 12

This script fixes an issue with the Ableton Push 2 where pads require more pressure to trigger clips in **session mode** and **sequencer mode** compared to note mode.

## What it does

It runs in the background and listens for mode changes on the Push 2. Every time Ableton resets the pad sensitivity, the script immediately reapplies the more responsive setting.

## Requirements

- Ableton Live 12
- Python 3.12 — download at [python.org](https://www.python.org/downloads/release/python-3120/) (check **"Add Python to PATH"** during installation)
- Install the required library by running this command once in your terminal:

```
py -3.12 -m pip install mido
```

## How to use

1. Download `push2_sensitivity.py` and `Start_Push2_Sensitivity.bat` and place them in the same folder
2. Open Ableton Live
3. Double-click `Start_Push2_Sensitivity.bat` — a small window will appear in the background
4. That's it! Keep the window open while using Ableton

## Note

The script is set up for a specific MIDI port configuration (output index 1, input index 0). If it doesn't work for you, you may need to adjust the `OUT_PORT_INDEX` and `IN_PORT_INDEX` values at the top of `push2_sensitivity.py`.

To find the correct index for your setup, run this in your terminal:

```python
import mido
print(mido.get_output_names())
print(mido.get_input_names())
```

---

*Created with the help of AI ([Claude](https://claude.ai) by Anthropic).*
