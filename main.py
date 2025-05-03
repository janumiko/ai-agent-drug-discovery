from query_processing import is_synthesis_query, extract_smiles
from retrosynthesis_integration import run_retrosynthesis
from response_generation import generate_response


def main():
    # Get the user's query (input can be replaced with API integration)
    user_query = input("Enter your query: ")

    # Step 1: Check if the query is about synthesis
    if is_synthesis_query(user_query):
        # Step 2: Extract SMILES representation
        smiles = extract_smiles(user_query)
        if smiles:
            print(f"SMILES extracted: {smiles}")

            # Step 3: Run retrosynthesis using AiZynthFinder
            print("Running retrosynthesis...")
            routes = run_retrosynthesis(smiles)

            # Step 4: Generate response for the user
            response = generate_response(smiles, routes)
            print("\nResponse:")
            print(response)
        else:
            print("No valid SMILES representation found in the query.")
    else:
        print("The query is not about the synthesis of a compound.")


if __name__ == "__main__":
    main()