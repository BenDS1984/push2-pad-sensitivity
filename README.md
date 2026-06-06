# push2-pad-sensitivity
Push 2 pad sensitivity fix for Ableton Live 12 — keeps pads responsive across all modes.
This script fixes an issue with the Ableton Push 2 where pads require more pressure to trigger clips in session mode and sequencer mode compared to note mode.
What it does
It runs in the background and listens for mode changes on the Push 2. Every time Ableton resets the pad sensitivity, the script immediately reapplies the more responsive setting.
Requirements

Ableton Live 12
Python 3.12 — download at python.org (check "Add Python to PATH" during installation)
Run this command once in your terminal to install the required library:
py -3.12 -m pip install mido

How to use

Download push2_sensitivity.py and Start_Push2_Sensitivity.bat and place them in the same folder
Open Ableton Live
Double-click Start_Push2_Sensitivity.bat — a small window will appear in the background
That's it! Keep the window open while using Ableton

Note
The script is set up for my specific MIDI port configuration (output index 1, input index 0). If it doesn't work for you, you may need to adjust the OUT_PORT_INDEX and IN_PORT_INDEX values at the top of push2_sensitivity.py.
Created with the help of AI (Claude by Anthropic).
