"""
Script principal pentru demonstrarea calculului distanței Manhattan.

Acest script citește date de intrare dintr-un fișier extern, calculează distanța 
Manhattan folosind o implementare proprie și o compară cu rezultatul oferit 
de biblioteca de specialitate SciPy.
"""

from util.calcule import distanta_manhattan_manual
from scipy.spatial.distance import cityblock

def incarca_vectori(cale_fisier):
    """
    Extrage vectorii numerici dintr-un fișier text specificat.

    Fișierul trebuie să conțină exact două linii, fiecare linie reprezentând 
    un vector cu elemente separate prin spațiu.

    Args:
        cale_fisier (str): Calea relativă sau absolută către fișierul .txt.

    Returns:
        tuple: O pereche (v1, v2) unde fiecare element este o listă de float-uri.
    """
    with open(cale_fisier, 'r') as f:
        linii = f.readlines()
        v1 = [float(x) for x in linii[0].split()]
        v2 = [float(x) for x in linii[1].split()]
    return v1, v2


if __name__ == "__main__":
    try:
        v1, v2 = incarca_vectori("date.txt")
        
        rezultat_manual = distanta_manhattan_manual(v1, v2)
        rezultat_scipy = cityblock(v1, v2)
        
        print(f"Vector 1: {v1}")
        print(f"Vector 2: {v2}")
        print(f"Distanta Manhattan (Manual): {rezultat_manual}")
        print(f"Distanta Manhattan (SciPy): {rezultat_scipy}")
        
    except FileNotFoundError:
        print("Eroare: Fisierul date.txt nu a fost gasit.")