# (!) Analyse de Signal Électrocardiogramme (ECG): 

+Simulation d'un signal cardiaque "propre" à partir d'un signal brut bruité qui simule des interférences électromagnétique réelles, ce projet cherche à démontrer l'importance du traitement numérique des signaux dans les dispositifs médicaux modernes.

## Fonctionnalités:
- **Génération du signal**: Simulation d'une onde ECG réaliste.
- **Injection du bruit**: Afin de répliquer les intérferences produites dans des conditions réelles.
- **Traitement du signal**: Élimination des intérferences à l'aide d'un filtre pass-bas (Filtre de Butterworth de cinquième ordre)
- **Visualisation**: Projection des résultats dans un graphe facile à lire.
- **Analyse:** Traitement des résultats, calcul du BPM via les pics du graphe.

## Outils:
- **Langage**: Python
- **IDE**: PyCharm
- **Bibliothèques**: "NumPy" (Pour les calculs mathématiques)
                     ,"SciPy" (Pour le traitement du signal et la détéction des pics)
                     ,"Matplotlib" (Pour la visualisation graphique de l'onde)

## Résultats:
Le script génère un graphe comparatif:
- **Signal Brut (bleu)**: Le signal avec interférences.
- **Signal Filtré (rouge)**: Le signal nettoyé prêt pour l'analyse médicale.

<img width="593" height="260" alt="image" src="https://github.com/user-attachments/assets/db6b6c3f-3f43-474c-9ea6-7315cd273b3a" />


->*Le script contient aussi un algorithme capable d'analyser le graphe et en déduire les battements par minutes du coeur (BPM) grâce au pics du signal filtré.*


<img width="579" height="272" alt="image" src="https://github.com/user-attachments/assets/5f3d4828-aa45-4a2a-8fca-c8b020abede8" />

## Remarques:
-> En ajustant la fréquence de coupure et l'ordre du filtre, il est possible d'optimiser le rapport signal sur bruit.

> b, a = signal.buffer("ordre", "fréquence de coupure")

## Réflexion:
-> Ce projet m'a permis de comprendre comment l'informatique peut sauver des vies en rendant les diagnostiques plus précis, même avec des capteurs à bas coût.


