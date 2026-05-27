# Orbital MFA: Kinetic satellite authorization

### What is this?
This project is a simulation of a secure ground-to-space authentication system. Most systems rely on static passwords that are easy to intercept. This project uses a Kinetic Signature a sequence of values representing things like signal burst timing or pressure, that must match a master key stored on the satellite.

I built this to get hands-on with Object Oriented Programming (OOP) and to see how security concepts like Replay Attack Protection and Mean Squared Error (MSE) verification actually work in code.

### How it Works
The system is built around three main parts:

* **The Satellite:** This class handles the satellite's internal state. It keeps the master key private and maintains a "burn list" of used IDs (nonces). If it sees an ID it has seen before, it flags a replay attack and kills the request immediately.
* **The Command:** This is a simple object used to package the user's action, their signature, and the unique ID for that specific transmission.
* **The Math Engine (`verify_signature`):** Instead of a rigid "correct or incorrect" check, this function calculates the average squared error between the input and the key. If the user’s input is "close enough" (within a 0.05 threshold), the satellite grants access.

### File Structure
* `project.py`: The core logic. It contains the `Satellite` and `Command` classes and the functions for parsing user input and checking signatures.
* `test_project.py`: A suite of `pytest` functions to make sure the math engine, input parser, and nonce generator aren't broken.
* `requirements.txt`: Minimal dependencies (mostly just `pytest`).

### Installation and Usage
To fire up the satellite simulator:
```bash
python project.py