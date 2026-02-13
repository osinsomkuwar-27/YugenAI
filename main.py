from message_generator import generate_messages
from knowledge_base import save_record


if __name__ == "__main__":
    sample_profile = """
    Rahul Sharma
    Founder at AI Labs
    Building AI automation tools for startups 🚀
    Passionate about AI, SaaS, and scaling fast.
    """

    results = generate_messages(sample_profile)

    print("\n===== Extracted Persona =====")
    print(results["persona"])

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
