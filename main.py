from message_generator import generate_messages
from knowledge_base import save_record
from input_handler import process_input


def run_system():

    print("\n🚀 YūgenAI - Offline Outreach Engine\n")

    user_input = input("Paste LinkedIn profile text or URL:\n\n")

    if not user_input.strip():
        print("\n❌ No input provided. Exiting.")
        return

    # Process input (detect URL / website / raw text)
    processed_text = process_input(user_input)

    # If LinkedIn URL detected (blocked scraping)
    if "[LinkedIn URL detected]" in processed_text:
        print(processed_text)
        return

    # Generate outreach messages
    print("\n🔍 Extracting persona and generating outreach...\n")

    results = generate_messages(processed_text)

    # Display persona
    print("===== Extracted Persona =====")
    print(results["persona"])

    # Display generated messages
    print("\n===== Generated Messages =====")
    print(results["full_output"])

    # Save to knowledge base
    save_record(
        results["persona"],
        {
            "combined_output": results["full_output"]
        }
    )

    print("\n✅ Record saved to knowledge_base.json")


if __name__ == "__main__":
    run_system()
