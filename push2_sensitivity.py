import mido
import time

# Instellingen
OUT_PORT_INDEX = 1
IN_PORT_INDEX = 0
SENSITIVITY = 0  # 0=regular, 1=reduced, 2=low

def send_sysex(port, data):
    msg = mido.Message('sysex', data=[0x00, 0x21, 0x1D, 0x01, 0x01] + data)
    port.send(msg)

def apply_sensitivity(port, sensitivity):
    send_sysex(port, [0x28, 0x00, 0x00, sensitivity])
    labels = ['regular', 'reduced', 'low']
    print(f"Pad settings toegepast: {labels[sensitivity]}")

out_ports = mido.get_output_names()
in_ports = mido.get_input_names()
out_port_name = out_ports[OUT_PORT_INDEX]
in_port_name = in_ports[IN_PORT_INDEX]

print(f"Output: {out_port_name}")
print(f"Input:  {in_port_name}")
print(f"Gevoeligheid: {SENSITIVITY}")
print("Gestart! Druk Ctrl+C om te stoppen.\n")

RESET_CONTROLS = [50, 51, 31, 52, 53, 47, 27, 118, 102, 21, 85]

with mido.open_output(out_port_name) as out_port:
    apply_sensitivity(out_port, SENSITIVITY)

    with mido.open_input(in_port_name) as in_port:
        try:
            for msg in in_port:
                if msg.type == 'control_change' and msg.control in RESET_CONTROLS and msg.value == 0:
                    time.sleep(0.15)
                    apply_sensitivity(out_port, SENSITIVITY)
                elif msg.type == 'pitchwheel' and msg.pitch == 0:
                    time.sleep(0.3)
                    apply_sensitivity(out_port, SENSITIVITY)
        except KeyboardInterrupt:
            print("\nGestopt.")
