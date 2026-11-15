#!/usr/bin/env python3
"""Guard requirements — OBC 2024, Part 9 (9.8.8) and Part 3 (3.3.1.18/3.4.6.5).
Usage: python3 guards.py part9|part3 LOCATION DROP_MM [industrial]
Part 9 locations: general dwelling_unit ext_low ext_high steps exit_flight exit_landing ext_10m
Part 3 locations: general exit_flight exit_landing ext_10m
A guard is required where the drop exceeds 600 mm (adjacent surface within 1.2 m).
"""
import json, os, sys

DATA = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "guard-data.json")))

def main():
    if len(sys.argv) < 4:
        print(__doc__); return
    part, loc, drop = sys.argv[1], sys.argv[2], float(sys.argv[3])
    industrial = len(sys.argv) > 4 and sys.argv[4] == "industrial"
    if drop <= 600:
        print(f"Drop {drop:g} mm: no guard required by 9.8.8.1 (threshold is more than 600 mm).")
        return
    table = DATA["heights_part9_mm"] if part == "part9" else DATA["heights_part3_mm"]
    h = table[loc]
    print(f"Guard REQUIRED (drop {drop:g} mm > 600 mm). Minimum height: {h['height']} mm — {h['basis']}")
    sphere = 200 if industrial else 100
    print(f"Openings: must prevent passage of a {sphere} mm sphere" + (" (industrial occupancy)." if industrial else "; triangular stair openings 150 mm sphere."))
    if part == "part9":
        print("Climbability: no member, attachment or opening between 140 mm and 900 mm above the walking surface may facilitate climbing (9.8.8.6).")

if __name__ == "__main__":
    main()
