#### Fonctions secondaires
"""
Ce module contient les fonctions pour générer et analyser la suite de Syracuse.
"""
# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """
    docsting pour le pylint de légères modifications ont été apportées pour le pilint
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')

#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n
    Args:
        n (int): la source de la suite
    Returns:
        list: la suite de Syracuse de source n
    """
    l= [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else :
            n = n*3 + 1
        l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    n = 0
    n = len(l)
    return n

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """
    n = 0
    altitude_initiale = l[0]
    for n in range(1, len(l)) :
        if l[n] < altitude_initiale :
            return n
    return n

def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    # votre code ici
    n = 0
    n = max(l)
    return n

#### Fonction principale
def main():
    """
    Exécute plusieurs tests sur la suite de Syracuse et affiche les résultats.
    """
    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))

    lsyr = syracuse_l(20)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))

if __name__ == "__main__":
    main()
