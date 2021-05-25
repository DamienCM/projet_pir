/*
 * Fichier contenant les fonctions nécessaires au bon fonctionnement du projet
 * 
 */

// Fonction signe 
static inline int8_t sgn(int val) {
 if (val < 0) return -1;
 if (val==0) return 0;
 return 1;
}
