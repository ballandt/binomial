"""Skript zur Ermittlung der Anzahl nötiger
Durchführungen eines binomialen Zufalls-
experimemts um mit einer gegebenen Wahrschein-
lichkeit eine bestimmte Anzahl von Treffern
einer gegebenen Einzelwahrscheinlichkeit
erwarten zu können."""


__author__ = "Camillo BALLANDT"


def comb(n, r):
    """Code für die Ermittlung des
    Binomialkoeffizienten bezogen
    von geeksforgeeks.com, bereitgestellt
    vom Nutzer rohan07."""
    if (r > n):
        return 0

    m = 1000000007
    inv = [0 for i in range(r + 1)]
    inv[0] = 1
    if (r + 1 >= 2):
        inv[1] = 1

    # Getting the modular inversion
    # for all the numbers
    # from 2 to r with respect to m
    # here m = 1000000007
    for i in range(2, r + 1):
        inv[i] = m - (m // i) * inv[m % i] % m

    ans = 1

    # for 1/(r!) part
    for i in range(2, r + 1):
        ans = ((ans % m) * (inv[i] % m)) % m

    # for (n)*(n-1)*(n-2)*...*(n-r+1) part
    for i in range(n, n - r, -1):
        ans = ((ans % m) * (i % m)) % m

    return ans


def binomcd(k, n, p):
    """Berechne die Wahrscheinlichkeit
    P(X<=k) eines Binomialen Zufalls-
    experiment"""
    P = 0
    for i in range(k+1):
        P += comb(n, i) * p**i * (1-p)**(n-i)
    return P


def finde_n(k, p, P):
    """Wendet Bisektionsverfahren auf
    die Funktion P(X>=k) in Abhängig-
    keit von n an, um das korrespon-
    dierende n zu ermitteln."""
    n0 = 0
    n1 = k + int(P/p)
    t = 0
    while True:
        t += 1
        P_n = 1 - binomcd(k-1, n1, p)   # Berechne P(n1)
        if P_n > P:   # P liegt zwischen P(n0) und P(n1)
            if n1 - n0 > 1:   # Zwischen n0 und n1 sind weitere ganze Zahlen
                n1 -= (n1 - n0) // 2   # Setze n1 auf den halben Abstand zwischen n0 und n1
            else:   # Es gibt keine ganzen Zahlen zwischen n0 und n1 - n1 ist das Ergebnis
                break
        elif P_n < P:   # P liegt nicht zwischen P(n0) und P(n1)
            n0, n1 = n1, n1 + n1 - n0   # Verschiebe n0 und n1 um den Abstand der beiden nach rechts
        else:
            break
    return n1


# Eingabe der Daten
k = int(input("k="))
p = eval(input("p="))
P = eval(input("P="))
# Ausgabe n
print(finde_n(k, p, P))
