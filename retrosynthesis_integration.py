from aizynthfinder.aizynthfinder import AiZynthFinder

def run_retrosynthesis(smiles: str):
    """
    Performs retrosynthesis for the given SMILES structure.

    Args:
        smiles (str): The SMILES representation of the target compound.

    Returns:
        list: A list of retrosynthetic routes or an empty list if no routes are found.
    """
    # # Set up logging for AiZynthFinder (optional)
    # setup_logger()

    # Initialize the AiZynthFinder instance with a configuration file
    finder = AiZynthFinder(configfile="config.yml")
    finder.smiles = smiles

    # Start the retrosynthesis search
    finder.tree_search()

    # Return retrosynthetic routes
    routes = finder.routes
    return routes


if __name__ == "__main__":
    smiles = "CC(=O)OC1=CC=CC=C1C(=O)O"

    print(f"Running retrosynthesis for SMILES: {smiles}")
    routes = run_retrosynthesis(smiles)

    if routes:
        print(f"Found {len(routes)} possible retrosynthetic routes!")
        # Example: Display the details of the first route
        print(routes[0].to_dict())
    else:
        print("No retrosynthetic routes found.")