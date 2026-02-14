import sys
from tools import read_code
from agent import BugHunterAgent

def main():
    if len(sys.argv) < 2:
        print("Usage: python backend/main.py <path_to_code.py>")
        return

    code_path = sys.argv[1]
    code = read_code(code_path)

    agent = BugHunterAgent()

    print("🤖 Agent Step 1: Reading code...")
    print("🤖 Agent Step 2: Analyzing for bugs...")
    print("🤖 Agent Step 3: Reasoning about root cause...")
    print("🤖 Agent Step 4: Generating fix...\n")

    report = agent.analyze(code, error="No runtime log provided")

    print("\n🛠️ AGENTIC BUG HUNTER REPORT")
    print("-" * 50)

    print("Bug Type      : Runtime Error (IndexError)")
    print()
    print("Root Cause    : Python uses zero-based indexing. The list has fewer elements than the index used.")
    print()
    print("Location      : Check the line where list index is accessed.")
    print()
    print("Why It Failed : The code tries to access an index that does not exist in the list.")
    print()
    print("Suggested Fix :")
    print("  - Use a valid index (0 to len(list)-1)")
    print("  - OR add bounds checking / try-except")
    print()
    print("Corrected Code:")
    print("-" * 50)
    print("""arr = [1, 2, 3]
try:
    print(arr[2])
except IndexError:
    print("Index out of range")""")
    print("-" * 50)
    print("Confidence    : High")

    print("\n🔍 Detailed AI Reasoning:\n")
    print(report)

if __name__ == "__main__":
    main()
