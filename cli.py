import argparse
from .scanner import scan_path

def main():
    parser = argparse.ArgumentParser(description="Sensitive Data Scanner")
    parser.add_argument("--path", required=True, help="Path to scan")
    args = parser.parse_args()

    results = scan_path(args.path)
    if not results:
        print("✅ No sensitive data found.")
    else:
        print("⚠️ Potential sensitive data detected:")
        for item in results:
            print(f"- {item['filename']} : {item['match_name']} => {item['match_value']}")

if __name__ == "__main__":
    main()
