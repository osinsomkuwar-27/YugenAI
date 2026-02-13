from message_generator import generate_messages

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

    print("\n===== Cold Email =====")
    print(results["email"])

    print("\n===== WhatsApp Message =====")
    print(results["whatsapp"])

    print("\n===== LinkedIn DM =====")
    print(results["linkedin"])

    print("\n===== Instagram DM =====")
    print(results["instagram"])

