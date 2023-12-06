import re

def extract_candidate_info(text):
    # Regular expressions for name and email extraction
    name_pattern = re.compile(r'\b(?:Mr\.|Ms\.|Mrs\.|Miss)?\s?([A-Za-z]+(?:\s[A-Za-z]+)*)\b')
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    # Search for name and email patterns in the text
    name_match = name_pattern.search(text)
    email_match = email_pattern.search(text)

    # Extract name and email if found, otherwise return 'N/A'
    candidate_name = name_match.group(1) if name_match else 'N/A'
    candidate_email = email_match.group(0) if email_match else 'N/A'

    return candidate_name, candidate_email
