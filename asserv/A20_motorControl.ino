/*
 * Fichier contenant les fonctions de controle des moteurs
 * 
 */


 /*
 * Fonction générique du pilotation d'un moteur
 */
void mot(int speed, int motSpeed, int motSensA, int motSensB){
  if(sgn(speed) == 0){ // Vitesse nulle
    analogWrite(motSpeed, 0);
    digitalWrite(motSensA, LOW);
    digitalWrite(motSensB, LOW);
  }
  if(sgn(speed)== 1){
    if(speed > 255){
      speed = 255;
    }
    analogWrite(motSpeed, speed);
    digitalWrite(motSensA, LOW);
    digitalWrite(motSensB, HIGH);
  } else {
    if(-speed > 255){
      speed = -255;
    }
    analogWrite(motSpeed, - speed);
    digitalWrite(motSensA, HIGH);
    digitalWrite(motSensB, LOW);
  }
}

// Fonctions individuelles de pilotage d'un moteur
void mot1(int speed){
  mot(speed, mot1speed, mot1sensA, mot1sensB);
}

void mot2(int speed){
  mot(speed, mot2speed, mot2sensA, mot2sensB);
}

void mot3(int speed){
  mot(speed, mot3speed, mot3sensA, mot3sensB);  
}
