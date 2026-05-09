# Théorème de Sturm — Comptage des racines réelles d'un polynôme

**Auteur :** Romuald Folly-Dogba

---

## Aperçu

Ce projet présente une implémentation algorithmique du **théorème de Sturm** en Python. Cet outil mathématique permet de déterminer le nombre exact de racines réelles distinctes d'un polynôme sur un intervalle donné $[a, b]$.

L'objectif principal de ce projet est de construire de bout en bout la logique mathématique requise, allant de la représentation bas niveau des polynômes et de la division euclidienne jusqu'à la génération de la suite de Sturm et au comptage des variations de signe.

---

## Architecture du Projet

```text
.
├── projet.ipynb       # Notebook principal avec l'implémentation et les cas pratiques
├── project_utils.py   # Fonctions utilitaires (formatage et affichage HTML)
├── Projet_ISM.pdf     # Rapport détaillé sur la théorie et la démarche du projet
└── README.md
```

---

## Détails de l'Implémentation

Le cœur algorithmique s'articule autour de deux composants majeurs, développés de manière à expliciter les mécanismes internes sans recourir à des boîtes noires de calcul symbolique formel.

### 1. Structure de données polynomiale (Classe `P`)
Cette classe gère la représentation d'un polynôme de degré $n$ à l'aide de ses coefficients (utilisant les tableaux `numpy` pour l'efficacité). Elle intègre les méthodes fondamentales d'algèbre polynomiale :
- L'évaluation numérique du polynôme en un point $x$.
- Le calcul algébrique de la dérivée formelle $P'(x)$.
- La **division euclidienne polynomiale** pour calculer le quotient et le reste. C'est l'opération critique qui sous-tend l'algorithme d'Euclide étendu nécessaire à la suite de Sturm.

### 2. Séquence de Sturm (Classe `SturmSequence`)
Cette classe implémente la logique du théorème. Pour un polynôme donné $P$, elle construit itérativement la suite de polynômes $(P_0, P_1, P_2, \dots, P_m)$ définie par :
- $P_0 = P$
- $P_1 = P'$
- $P_{i} = -\text{Reste}(P_{i-2} \div P_{i-1})$ pour $i \ge 2$, jusqu'à l'obtention d'une constante.

Une fois la séquence générée, le nombre de racines sur un intervalle $[a, b]$ est déduit par la formule $V(a) - V(b)$, où $V(x)$ représente le nombre de changements de signe stricts dans la séquence évaluée en $x$.

---

## Cas Pratiques et Validation

Le notebook `projet.ipynb` inclut l'exécution de l'algorithme sur différents cas :
1. **Cas d'étude spécifique :** Évaluation pas à pas sur le polynôme $P(x) = -\frac{1}{2}x^4 + \frac{1}{2}x^3 - 4x^2 - x - 6$.
2. **Génération aléatoire :** Tests de robustesse sur des polynômes générés de manière aléatoire pour valider le comptage sur divers intervalles.

Les résultats sont formatés sous forme de tableaux lisibles générés par le script `project_utils.py`.

---

## Exécution

Le projet est conçu pour être exécuté dans un environnement interactif Jupyter.

**Dépendances requises :**
- `numpy` (pour les opérations vectorielles sur les coefficients)
- `IPython` (pour l'affichage formaté des résultats)

**Instructions :**
1. Cloner le dépôt.
2. Ouvrir `projet.ipynb` via Jupyter Notebook, JupyterLab ou Google Colab.
3. Exécuter les cellules séquentiellement pour initialiser les classes et lancer les démonstrations.
