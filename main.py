import sys
from agent import run_agent


def print_usage_and_exit():
    print("Usage: python main.py \"<mission>\"")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage_and_exit()

    mission = sys.argv[1]
    print(f"Running mission: {mission}\n")
    result = run_agent(mission)
    print("\nResult:")
    print(result)
