from retrosynthesis_integration import run_retrosynthesis


def generate_response(smiles: str, synthesis_routes: list) -> str:
    """
    Generates a response for the user based on retrosynthesis results.

    Args:
        smiles (str): The SMILES target compound.
        synthesis_routes (list): Retrosynthetic routes provided by the AiZynthFinder.

    Returns:
        str: The generated response text for the user.
    """
    if not synthesis_routes:
        return f"No synthesis routes were found for the compound: {smiles}"

    # Use the best (first) retrosynthetic route
    best_route = synthesis_routes[0]

    # Construct the response
    response_parts = [
        f"Synthesis route for the compound: {smiles}:",
        f"1. Start with the following starting materials: {', '.join(best_route.starting_materials)}.",
        "2. Perform the reaction steps as follows:"
    ]
    for idx, step in enumerate(best_route.reaction_steps, start=1):
        response_parts.append(f"   {idx}. {step}.")

    # Combine and return all response parts
    return "\n".join(response_parts)


if __name__ == "__main__":
    smiles = "CC(=O)OC1=CC=CC=C1C(=O)O"
    routes = run_retrosynthesis(smiles)

    response = generate_response(smiles, routes)
    print(response)