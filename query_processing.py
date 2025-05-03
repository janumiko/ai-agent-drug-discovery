import re

def is_synthesis_query(user_query: str) -> bool:
    """
    Checks if a user's query is about the synthesis of a chemical compound.

    Args:
        user_query (str): User's input query.

    Returns:
        bool: True if the query is about synthesis, False otherwise.
    """
    synthesis_keywords = ["how to synthesize", "synthesis", "how to make", "synthesize"]
    return any(keyword in user_query.lower() for keyword in synthesis_keywords)

def extract_smiles(user_query: str) -> str:
    """
    Extracts a SMILES representation of a compound from the user's query.

    Args:
        user_query (str): User's input query.

    Returns:
        str: Extracted SMILES string or an empty string if no valid format is found.
    """
    # Define a regex pattern to capture potential SMILES strings
    smiles_pattern = r"[A-Za-z0-9@+\-\[\]\(\)=#$:.%]+"
    potential_smiles = re.findall(smiles_pattern, user_query)

    # Filter patterns to find the most likely SMILES string
    for smiles in potential_smiles:
        if len(smiles) > 3:  # Consider valid SMILES strings with length > 3
            return smiles
    return ""

if __name__ == "__main__":
    user_query = "How to synthesize CC(=O)OC1=CC=CC=C1C(=O)O?"
    if is_synthesis_query(user_query):
        smiles = extract_smiles(user_query)
        if smiles:
            print(f"The query is about the synthesis of the compound: {smiles}")
        else:
            print("No valid SMILES representation could be extracted.")
    else:
        print("The query is NOT about synthesis.")