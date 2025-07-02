import os
import shutil
import sys
from crew import literature_review_crew

def main():
    crew = literature_review_crew()

    file_path = input("📄 Enter your research paper file path: ").strip()

    if not os.path.exists(file_path):
        print("❌ File not found! Please check the path and try again.")
        sys.exit(1)

    print("✅ File found.")

    # Create docs/ directory if it doesn't exist
    os.makedirs("docs", exist_ok=True)

    # Copy the file into docs/
    file_name = os.path.basename(file_path)
    new_file_path = os.path.join("docs", file_name)
    shutil.copy(file_path, new_file_path)

    print(f"📁 File copied to: {new_file_path}")

    user_query = input("🤖 What do you want to learn from this paper? (Press enter to summarize normally): ").strip()

    
    result = crew.kickoff(inputs={
        "file_path": new_file_path,
        "user_query": user_query
    })

    # Save final report
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(result)

    print("\n📝 Summary saved to report.txt\n")

if __name__ == "__main__":
    main()
