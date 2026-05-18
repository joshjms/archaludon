"""Render the Da Vinci spec via arch.visualize."""
from pathlib import Path

from arch_sim.arch import load, visualize

SPEC = Path(__file__).resolve().parents[1] / "specs" / "da-vinci.yaml"
OUT = Path(__file__).with_name("da_vinci.png")


def main() -> None:
    print(f"wrote {visualize(load(SPEC), OUT)}")


if __name__ == "__main__":
    main()
