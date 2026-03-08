# MECE4613-A2 — Industrial Automation

**Columbia University — Department of Mechanical Engineering**
**Course:** MECE4613 Industrial Automation
**Instructor:** Ali Dadgar

---

## Overview

This repository contains the scripts and exercises for Assignment 2. The assignment covers three main sections:

- **Section A** — Python fundamentals and robot control (LED, touch sensors, motors)
- **Section B** — Building a robot command shell
- **Section C** — Web services for remote robot control (SSH, subprocess, HTTP/Tornado)

All scripts are designed to run on a **Raspberry Pi** with an **Adafruit CRICKIT HAT** attached.

---

## Getting Started

### 1. Connect to the Raspberry Pi via SSH

From your local machine, connect to the Raspberry Pi over the same Wi-Fi network:

```bash
ssh <your_uni>@<your_ip_address>
```

Example:

```bash
ssh di2256@192.168.132.175
```

### 2. Activate the Virtual Environment

**Before running any script**, activate the Python virtual environment:

```bash
source .venv/bin/activate
```

You should see `(.venv)` appear in your terminal prompt, confirming the environment is active.

### 3. Navigate to the Scripts Directory

```bash
cd ~/bin
```

### 4. Run a Script

```bash
python <script_name>.py
```

Example:

```bash
python controller01.py
```

---

## Scripts

### Section A: Python & Robot Control

| Script | Description | Type |
|--------|-------------|------|
| `controller01.py` | Basic LED color test — verifies Crickit connection | Learning |
| `controller02.py` | LED blinking loop with functions and parameters | Learning |
| `controller03.py` | GPIO/I2C device detection | Learning |
| `controller04.py` | Touch sensor status detection | Learning |
| `controller05-ex.py` | **Exercise** — Terminal input-driven LED color controller (1=Blue, 2=Green, 3=Red, 4=Exit) | Exercise |
| `controller06.py` | Basic motor drive for 0.5 seconds | Learning |
| `controller07-ex.py` | **Exercise** — Touch sensor triggers LED + motor drive | Exercise |
| `controller08.py` | Object-oriented Robot class with argparse | Learning |
| `controller09-ex.py` | **Exercise** — Motor sync calibration (forward/backward coefficients) | Exercise |
| `motor-ex.py` | **Exercise** — Reusable motor library with `functools.partial` | Exercise |

### Section B: Robot Shell

| Script | Description | Type |
|--------|-------------|------|
| `shell1.py` | Basic robot shell using `cmd` library | Learning |
| `shell2.py` | Shell with speed/duration arguments and quit command | Learning |
| `shell3-ex.py` | **Exercise** — Advanced shell with argument parsing | Exercise |

### Section C: Web Services

| Script | Description | Type |
|--------|-------------|------|
| `webservice1.py` | Remote script execution via SSH | Learning |
| `webservice2.py` | Remote execution using `subprocess` | Learning |
| `webservice3.py` | Tornado web server for robot control | Learning |
| `webservice4.py` | Tornado server with POST request handling | Learning |
| `webservice4-client1-exp.py` | **Exercise** — URL-based remote robot control | Exercise |
| `webservice4-client2-exp.py` | **Exercise / DEMO** — HTTP-based remote control with latency measurement | Exercise |

---

## Quick Reference

### SSH One-Liner (run a script remotely)

```bash
ssh <your_uni>@<your_ip_address> 'source .venv/bin/activate && python ~/bin/webservice1.py spin_left --duration 1 --speed 3'
```

### Copy scripts to Pi

```bash
scp *.py <your_uni>@<your_ip_address>:/home/<your_uni>/bin/
```

### Motor control via CLI (controller08)

```bash
python controller08.py -l 0.5 -r 0.5 -d 2
```

### Web service test (curl)

```bash
curl http://<your_ip_address>:8888/
curl http://<your_ip_address>:8888/forward
curl -X POST http://<your_ip_address>:8888/spin_right -d '{"duration": 1, "speed": 3}'
```

---

## Hardware Requirements

- Raspberry Pi (with USB flash drive or SD card)
- Adafruit CRICKIT HAT (connected via GPIO)
- DC Motors (×2) — connected to CRICKIT motor ports
- Power bank — USB-A to CRICKIT power jack
- Wi-Fi network — same network as your local machine

---

## Dependencies

Installed inside the virtual environment (`.venv`):

- `adafruit-circuitpython-crickit`
- `tornado` (for web services in Section C)

---

## Submission

Exercise scripts (files ending in `-ex.py`) should be zipped and uploaded to Courseworks by the due date.

```bash
zip exercises.zip *-ex.py *-exp.py
```
