import re

log_lines = """Sphere 1, 0.0s, GT: Initializing Simulation, Galactic Garden
Sphere 2, 0.0s, GT: Initializing Simulation, Galactic Garden
Sphere 1, 0.0s, GT: Terminal Output
...
Sphere 1, 251.0s, GT: ======================== End of Game ========================""".splitlines()

log_events = []
for line in log_lines:
    m = re.match(r"Sphere (\d), ([\d\.]+)s, GT: (.*)", line)
    if m:
        sphere, time, msg = m.groups()
        log_events.append({
            "time": float(time),
            "sphere": int(sphere),
            "msg": msg.strip()
        })
# Now log_events is your array!
