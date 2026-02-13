import json
import os
import uuid
from datetime import datetime

KB_FILE = "knowledge_base.json"

def init_kb():
    if not os.path.exists(KB_FILE):
        with open(KB_FILE, "w") as f:
            json.dump({"records": []}, f, indent=4)

def save_record(persona, messages):

    init_kb()

    with open(KB_FILE, "r") as f:
        kb = json.load(f)

    entry = {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "persona": persona,
        "messages": messages
    }

    kb["records"].append(entry)

    with open(KB_FILE, "w") as f:
        json.dump(kb, f, indent=4)

    return entry
