"""
Modul utilitar pentru calcule matematice în Inteligența Artificială.

Acest modul conține implementări manuale ale unor metrici de distanță,
utilizate pentru a înțelege fundamentele algoritmilor de învățare automată.
"""

def distanta_manhattan_manual(vector1, vector2):
    """
    Calculează distanța Manhattan (L1 Norm) între doi vectori numerici.

    Distanța Manhattan este suma diferențelor absolute ale coordonatelor corespondente:
    d(x, y) = sum(|xi - yi|)

    Args:
        vector1 (list[float]): Prima listă de numere reprezentând coordonatele primului vector.
        vector2 (list[float]): A doua listă de numere reprezentând coordonatele celui de-al doilea vector.

    Returns:
        float: Valoarea distanței Manhattan dintre cei doi vectori.

    Raises:
        ValueError: Dacă vectorii furnizați nu au aceeași lungime.
        
    Example:
        >>> distanta_manhattan_manual([1, 2], [4, 6])
        7.0
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vectorii trebuie să aibă aceeași dimensiune pentru a calcula distanța.")
    
    return sum(abs(a - b) for a, b in zip(vector1, vector2))