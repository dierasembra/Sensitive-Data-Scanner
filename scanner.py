import os, re, json

def load_patterns():
    path = os.path.join(os.path.dirname(__file__), "patterns.json")
    with open(path, "r") as f:
        return json.load(f)

def scan_file(filepath, patterns):
    findings = []
    try:
        with open(filepath, "r", errors="ignore") as f:
            content = f.read()
            for name, pattern in patterns.items():
                for match in re.findall(pattern, content):
                    findings.append((name, match))
    except:
        pass
    return findings

def scan_path(path):
    patterns = load_patterns()
    results = []
    if os.path.isfile(path):
        items = scan_file(path, patterns)
        for name, value in items:
            results.append({"filename": path, "match_name": name, "match_value": value})
    else:
        for root, dirs, files in os.walk(path):
            for file in files:
                fp = os.path.join(root, file)
                items = scan_file(fp, patterns)
                for name, value in items:
                    results.append({"filename": fp, "match_name": name, "match_value": value})
    return results
