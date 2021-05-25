/*
 * Projet d'intégration Robotique (PIR)
 * Cartier-Millon Damien
 * Doppler Luc
 * Lepré Maxime
 * Niddam Ethan
 * 
 * 22 mai 2021
 * 
 */

 // Ajout des bibliothèques utilisées
#include <Encoder.h>

// Définition des pins d'entrée et de sortie
#define cod1A 23
#define cod1B 22
#define mot1speed 3
#define mot1sensA 5
#define mot1sensB 4

#define cod2A 21
#define cod2B 20
#define mot2speed 0
#define mot2sensA 2
#define mot2sensB 1

#define cod3A 19
#define cod3B 18
#define mot3speed 6
#define mot3sensA 7
#define mot3sensB 8

#define buzzer 13

#define led1 9
#define led2 10
#define led3 11
#define led4 12

#define servo1 17
#define servo2 16
#define servo3 15
#define servo4 14


// Définition des encodeurs
Encoder cod1(cod1A, cod1B);
Encoder cod2(cod2A, cod2B);
Encoder cod3(cod3A, cod3B);

// Timer nécessaire pour cadencer l'asservissement
IntervalTimer TMR1; //TEENSY ONLY

// Variables nécessaires

// Lecture de la liaison série
String dataSerie = "";

// Fréquence d'asservissement
int freqAsserv = 10000; // en micro secondes -> 10ms

// Valeurs cibles
long thetaCible1 = 0; 
long thetaCible2 = 0; 
long thetaCible3 = 0;

long RPMCible1 = 0;
long RPMCible2 = 0;
long RPMCible3 = 0;

// Pas position
const int pas = 660;

void setup(){
  pinMode(mot1speed, OUTPUT);
  pinMode(mot1sensA, OUTPUT);
  pinMode(mot1sensB, OUTPUT);

  pinMode(mot2speed, OUTPUT);
  pinMode(mot2sensA, OUTPUT);
  pinMode(mot2sensB, OUTPUT);

  pinMode(mot3speed, OUTPUT);
  pinMode(mot3sensA, OUTPUT);
  pinMode(mot3sensB, OUTPUT);

  pinMode(servo1, OUTPUT);
  pinMode(servo2, OUTPUT);
  pinMode(servo3, OUTPUT);
  pinMode(servo4, OUTPUT);

  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);

  pinMode(buzzer, OUTPUT);

  Serial.begin(9600);
  delay(10);

  // Tous les moteurs sont arrêtés
  mot1(0);
  mot2(0);
  mot3(0);

  // Appel à fréquence fixe
  TMR1.begin(asservPos, freqAsserv); // Appel à l'asservissement en position toutes les 10ms
}
 
void loop(){
  if(Serial.available() > 0){
    dataSerie = Serial.readStringUntil('\n');
  }

  if(dataSerie.length() != 0){
    Serial.println(dataSerie);
  }

  if(dataSerie.equals("RB")){
    // Nécessaire si on envoie des commandes après B
    clearCibles();
    // On redémarre l'asservissement en position
    TMR1.begin(asservPos, freqAsserv);
    dataSerie= "";
  }

  if(dataSerie.equals("LB")){
    // Nécessaire si on envoie des commandes après B
    clearCibles();
    // On redémarre l'asservissement en vitesse
    TMR1.begin(asservRPM, freqAsserv);
    dataSerie="";
  }

  if(dataSerie.equals("Y")){
    // Test du moteur 1
    RPMCible1 = 200;
    RPMCible2 = 200;
    RPMCible3 = 200;
    dataSerie ="";
  }
  

  if(dataSerie.equals("B")){
    // On arrête l'asservissement
    TMR1.end(); 
    // On coupe les moteurs
    mot1(0);
    mot2(0);
    mot3(0);
    // On clear les consignes
    clearCibles();
    dataSerie = "";
  }

  if(dataSerie.equals("R")){
    // choixAsservPos(true);
    thetaCible1 += pas;
    thetaCible2 += pas;
    thetaCible3 += pas;
    RPMCible1 = 200;
    RPMCible2 = 200;
    RPMCible3 = 200;
    dataSerie = "";
  }

  if(dataSerie.equals("L")){
    // choixAsservPos(true);
    thetaCible1 -= pas;
    thetaCible2 -= pas;
    thetaCible3 -= pas;
    RPMCible1 = -200;
    RPMCible2 = -200;
    RPMCible3 = -200;
    dataSerie = "";
  }


  if(dataSerie.equals("PU")){
    // choixAsservPos(true);
    // Avancer
    // thetaCible1 CONSTANT
    thetaCible2 += 660;
    thetaCible3 -= 660;
    dataSerie = "";
  }

  if(dataSerie.equals("PD")){
    // choixAsservPos(true);
    // Reculer
    thetaCible2 -= 10 * 147;
    thetaCible3 += 8 * 147;
    dataSerie = "";
    
  }

  if(dataSerie.equals("PR")){
    // choixAsservPos(true);
    // Gauche
    thetaCible1 += 4*170;
    thetaCible2 -= 4*85;
    thetaCible3 -= 4*85;
    dataSerie = "";
  }

  if(dataSerie.equals("PL")){
    // choixAsservPos(true);
    // Droite
    thetaCible1 -= 4*170;
    thetaCible2 += 4*84;
    thetaCible3 += 4*84;
    dataSerie = "";
  }

  if(dataSerie.charAt(0) == 'u'){
    dataSerie.remove(0,1);
    RPMCible2 = -dataSerie.toInt();    
  }

  if(dataSerie.charAt(0) == 'v'){
    dataSerie.remove(0,1);
    RPMCible1 = -dataSerie.toInt();   
  }

  if(dataSerie.charAt(0) == 'w'){
    dataSerie.remove(0,1);
    RPMCible3 = -dataSerie.toInt();   
  }
  

  if(dataSerie.equals("X")){
    tone(buzzer, 440,1000);
    dataSerie = ""; 
  }

  Serial.println("ICI");
  Serial.println(String(cod1.read()) + " - " + String(cod2.read()) + " - " + String(cod3.read()));
  Serial.println(String(thetaCible1) + " - " + String(thetaCible2) + " - " + String(thetaCible3));
}
 
