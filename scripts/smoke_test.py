# scripts/smoke_test.py
from your_project import __version__

def main() -> None:
    print("Smoke OK. Version:", __version__)

if __name__ == "__main__":
    main()
