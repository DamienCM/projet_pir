#include <Encoder.h>

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


Encoder cod1(cod1A, cod1B);
Encoder cod2(cod2A, cod2B);
Encoder cod3(cod3A, cod3B);

IntervalTimer TMR1; //TEENSY ONLY

// type d'asserv
int typeAss = 0; // 0 asservissement en pos 1 ass en vitesse

// Ticks par tour
const double ticks = 660.0;

// Coeff PID
// Theta
const double Kp1_theta = 1;
const double Ki1_theta = 0.2;
const double Kd1_theta = 0.1;

const double Kp2_theta = 1;
const double Ki2_theta = 0.2;
const double Kd2_theta = 0.1;

const double Kp3_theta = 1;
const double Ki3_theta = 0.2;
const double Kd3_theta = 0.1;

// RPM
const double Kp1_rpm = 1;
const double Ki1_rpm = 0.2;
const double Kd1_rpm = 0.1;

const double Kp2_rpm = 1;
const double Ki2_rpm = 0.2;
const double Kd2_rpm = 0.1;

const double Kp3_rpm = 1;
const double Ki3_rpm = 0.2;
const double Kd3_rpm = 0.1;

// Valeurs cibles
long thetaCible1 = 0; // 2* ticks;
long thetaCible2 = 0; // 2 * ticks;
long thetaCible3 = 0; // 2 * ticks;

long RPMCible1 = 0;
long RPMCible2 = 0;
long RPMCible3 = 0;

// Temps
long tps1 = millis();
long tpsOld1 = 0;

long tps2 = millis();
long tpsOld2 = 0;

long tps3 = millis();
long tpsOld3 = 0;

// erreur 
double erreur1;
double erreurOld1 = 0;
double integrale1;
double integraleOld1 = 0;
double derivee1;

double erreur2;
double erreurOld2 = 0;
double integrale2;
double integraleOld2 = 0;
double derivee2;

double erreur3;
double erreurOld3 = 0;
double integrale3;
double integraleOld3 = 0;
double derivee3;

const double precision = 2; // essayer d'avoir 1 ou 2 en précision

// Positions réelles
long cod1Theta = cod1.read();
long cod1ThetaOld = cod1.read();

long cod2Theta = cod2.read();
long cod2ThetaOld = cod2.read();

long cod3Theta = cod3.read();
long cod3ThetaOld = cod3.read();

String dataIn;


void setup(){
  // Initialisation des pins
  pinMode(cod1A, INPUT);
  pinMode(cod1B, INPUT);
  pinMode(mot1speed, OUTPUT);
  pinMode(mot1sensA, OUTPUT);
  pinMode(mot1sensB, OUTPUT);

  pinMode(cod2A, INPUT);
  pinMode(cod2B, INPUT);
  pinMode(mot2speed, OUTPUT);
  pinMode(mot2sensA, OUTPUT);
  pinMode(mot2sensB, OUTPUT);

  pinMode(cod3A, INPUT);
  pinMode(cod3B, INPUT);
  pinMode(mot3speed, OUTPUT);
  pinMode(mot3sensA, OUTPUT);
  pinMode(mot3sensB, OUTPUT);
    
  // Initialisation de la liaison série
  Serial.begin(9600);
  delay(10);


  // Début de l'asserv en position
  if(typeAss == 0){
    TMR1.begin(asservPos, 10000);
  } else {
    TMR1.begin(asservRPM, 10000);
  }
  
}



void loop(){
  // Serial.println(RPMCible1);
  if(Serial.available() > 0){
    dataIn = Serial.readStringUntil('\n');

    // PANIC Button -> tous les moteurs sont mis à l'arrêt
    if(dataIn.equals("B")){
      choixAss(1);
      RPMCible1 = 0;
      RPMCible2 = 0;
      RPMCible3 = 0;
    }
    
    if(dataIn.equals("R")){
      choixAss(0);
      thetaCible1 += ticks;
      thetaCible2 += ticks;
      thetaCible3 += ticks;
    }

    if(dataIn.equals("L")){
      choixAss(0);
      thetaCible1 -= ticks;
      thetaCible2 -= ticks;
      thetaCible3 -= ticks;      
    }

    if(dataIn.equals("PU")){
      choixAss(0);
      thetaCible1 += ticks;
      // thetaCible2 -= ticks;
      thetaCible3 -= ticks;      
    }

    if(dataIn.equals("PD")){
      choixAss(0);
      thetaCible1 -= ticks;
      // thetaCible2 -= ticks;
      thetaCible3 += ticks;      
    }

    if(dataIn.equals("X")){
      tone(buzzer, 440,3000);
    }

/*
    if(dataIn.equals("PL")){
      thetaCible1 -= ticks;
      thetaCible2 -= ticks;
      thetaCible3 -= ticks;      
    }

    if(dataIn.equals("PR")){
      thetaCible1 -= ticks;
      thetaCible2 -= ticks;
      thetaCible3 -= ticks;      
    }

    */

    if(dataIn.charAt(0) == 'u'){
      choixAss(1);
      dataIn.remove(0,1);
      RPMCible2 = -dataIn.toInt();
    }

    if(dataIn.charAt(0) == 'v'){
      choixAss(1);
      dataIn.remove(0,1);
      RPMCible1 = -dataIn.toInt();
    }

    if(dataIn.charAt(0)=='w'){
      choixAss(1);
      dataIn.remove(0,1);
      RPMCible3 = -dataIn.toInt();
    }

    if(dataIn.equals("B")){
      choixAss(1);
      RPMCible1 = 0;
      RPMCible2 = 0;
      RPMCible3 = 0;
    }
  }
}


void choixAss(int choixAss){ // 0-> pos; 1-> vit
  if(choixAss != typeAss){
    if(choixAss == 0){
      // On veut un asserv en position
      TMR1.end();
      TMR1.begin(asservPos, 10000);
      typeAss = 0;      
    }
    if(choixAss == 1){
      // On veut un asserv en vitesse
      TMR1.end();
      TMR1.begin(asservRPM, 10000);
      typeAss = 1;
    }
    // On clean toutes les valeurs liées aux PIDs
    erreur1= 0;
    erreurOld1 = 0;
    integrale1 = 0;
    integraleOld1 = 0;
    derivee1 = 0;
    
    erreur2 = 0;
    erreurOld2 = 0;
    integrale2 = 0;
    integraleOld2 = 0;
    derivee2 = 0;
    
    erreur3 = 0;
    erreurOld3 = 0;
    integrale3 = 0;
    integraleOld3 = 0;
    derivee3 = 0;
    
  }
}


void asservPos(){
  
  ISR_asserv_PID(cod1Theta, cod1ThetaOld, Kp1_theta, Ki1_theta, Kd1_theta, thetaCible1, tps1, tpsOld1, erreur1, erreurOld1, integrale1, integraleOld1, derivee1, precision, ticks, 1, 0); // Asservissement en position du moteur 1
  ISR_asserv_PID(cod2Theta, cod2ThetaOld, Kp2_theta, Ki2_theta, Kd2_theta, thetaCible2, tps2, tpsOld2, erreur2, erreurOld2, integrale2, integraleOld2, derivee2, precision, ticks, 2, 0);
  ISR_asserv_PID(cod3Theta, cod3ThetaOld, Kp3_theta, Ki3_theta, Kd3_theta, thetaCible3, tps3, tpsOld3, erreur3, erreurOld3, integrale3, integraleOld3, derivee3, precision, ticks, 3, 0);

}

void asservRPM(){
  /*
  ISR_asserv_PID(cod1Theta, cod1ThetaOld, Kp1_theta, Ki1_theta, Kd1_theta, thetaCible1, tps1, tpsOld1, erreur1, erreurOld1, integrale1, integraleOld1, derivee1, precision, ticks, 1, 0); // Asservissement en position du moteur 1
  ISR_asserv_PID(cod2Theta, cod2ThetaOld, Kp2_theta, Ki2_theta, Kd2_theta, thetaCible2, tps2, tpsOld2, erreur2, erreurOld2, integrale2, integraleOld2, derivee2, precision, ticks, 2, 0);
  ISR_asserv_PID(cod3Theta, cod3ThetaOld, Kp3_theta, Ki3_theta, Kd3_theta, thetaCible3, tps3, tpsOld3, erreur3, erreurOld3, integrale3, integraleOld3, derivee3, precision, ticks, 3, 0);
*/

  ISR_asserv_PID(cod1Theta, cod1ThetaOld, Kp1_theta, Ki1_theta, Kd1_theta, RPMCible1, tps1, tpsOld1, erreur1, erreurOld1, integrale1, integraleOld1, derivee1, precision, ticks, 1, 1); // Asservissement en position du moteur 1
  ISR_asserv_PID(cod2Theta, cod2ThetaOld, Kp2_theta, Ki2_theta, Kd2_theta, RPMCible2, tps2, tpsOld2, erreur2, erreurOld2, integrale2, integraleOld2, derivee2, precision, ticks, 2, 1);
  ISR_asserv_PID(cod3Theta, cod3ThetaOld, Kp3_theta, Ki3_theta, Kd3_theta, RPMCible3, tps3, tpsOld3, erreur3, erreurOld3, integrale3, integraleOld3, derivee3, precision, ticks, 3, 1);
  
}


void ISR_asserv_PID(long& codTheta, long& codThetaOld, double Kp, double Ki, double Kd, long& Cible, long& tps, long& tpsOld, double& erreur, double& erreurOld, double& integrale, double& integraleOld, double& derivee, double precision, double ticks, unsigned int moteur, unsigned int type){
  // Mise à jour de la position angulaire
  switch(moteur){
    case 1:
      codTheta = cod1.read();
      break;
    case 2:
      codTheta = cod2.read();
      break;
    case 3:
      codTheta = cod3.read();
      break;
  }
  // Calcul du delta de temps
  tps = millis();
  long deltaTps;
  deltaTps = tps - tpsOld;
  
  // Calcul du delta de position
  long deltaTheta;
  deltaTheta = codTheta - codThetaOld;

  // Calcul de la vitesse
  double RPM;
  RPM = (deltaTheta/(deltaTps/1000))*60;

  if(type == 0){ // Asserv en position
    erreur = Cible - codTheta;
    
  } else { // Asserv en vitesse
    erreur = Cible - RPM;
  }
  
  // Calcul de l'erreur
  // erreur = thetaCible - codTheta;
  integrale = integraleOld + (deltaTps*(erreur - erreurOld)/2);
  derivee = Kd * (erreur - erreurOld) / deltaTps ;

  // Calcul de la consigne
  int consigne = int(Kp * erreur + Ki * integrale + Kd * derivee);

  // Affichage sur le plotter
  
  //Serial.print(RPM);
  //Serial.print(thetaCible/ticks);
  //Serial.print(",");
  //Serial.print(codTheta);
  //Serial.print(",");
  //Serial.print(erreur);
  //Serial.print(integrale);
  // Serial.println();

  // Pilotage moteur
  if(abs(erreur) < precision){
    switch(moteur){
      case 1:
        mot1(0);
        break;
      case 2:
        mot2(0);
        break;
      case 3:
        mot3(0);
        break;
    }
  } else {
    switch(moteur){
      case 1:
        mot1(consigne);
        break;
      case 2:
        mot2(consigne);
        break;
      case 3:
        mot3(consigne);
        break;
    }
  }

  // Mise à jour des variables
  erreurOld = erreur;
  tpsOld = tps;
  codThetaOld = codTheta;
  integraleOld = integrale;
  

  return;
}


static inline int8_t sgn(int val) {
 if (val < 0) return -1;
 if (val==0) return 0;
 return 1;
}


void mot1(int speed){
  mot(speed, mot1speed, mot1sensA, mot1sensB);
}



void mot2(int speed){
  mot(speed, mot2speed, mot2sensA, mot2sensB);
}


void mot3(int speed){
  mot(speed, mot3speed, mot3sensA, mot3sensB);  
}




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
