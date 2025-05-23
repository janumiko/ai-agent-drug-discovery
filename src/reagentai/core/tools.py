from rdkit import Chem
from .registers import register_tool
import logging

logger = logging.getLogger(__name__)


@register_tool()
def is_valid_smiles(smiles: str, sanitize: bool = True) -> bool:
    """
    Check if a SMILES string is valid.
    
    Args:
        smiles (str): The SMILES string to check.
        sanitize (bool): Whether to sanitize the molecule. Default is True.
        
    Returns:
        bool: True if the SMILES string is valid, False otherwise.
    """
    try:
        mol = Chem.MolFromSmiles(smiles, sanitize=sanitize)
    except Exception:
        mol = None

    logging.info(f"SMILES: {smiles}, Valid: {mol is not None}")

    return mol is not None
