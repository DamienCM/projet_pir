/*
 * Fichier contenant les fonctions d'asservissement
 * 
 */


//PID Asserv généralisé
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


// Appel des PIDs en position
void asservPos(){
  ISR_asserv_PID(cod1Theta, cod1ThetaOld, Kp1_theta, Ki1_theta, Kd1_theta, thetaCible1, tps1, tpsOld1, erreur1, erreurOld1, integrale1, integraleOld1, derivee1, precision, ticks, 1, 0); // Asservissement en position du moteur 1
  ISR_asserv_PID(cod2Theta, cod2ThetaOld, Kp2_theta, Ki2_theta, Kd2_theta, thetaCible2, tps2, tpsOld2, erreur2, erreurOld2, integrale2, integraleOld2, derivee2, precision, ticks, 2, 0);
  ISR_asserv_PID(cod3Theta, cod3ThetaOld, Kp3_theta, Ki3_theta, Kd3_theta, thetaCible3, tps3, tpsOld3, erreur3, erreurOld3, integrale3, integraleOld3, derivee3, precision, ticks, 3, 0);
}


// Appel des PIDs en vitesse
void asservRPM(){
  ISR_asserv_PID(cod1Theta, cod1ThetaOld, Kp1_theta, Ki1_theta, Kd1_theta, RPMCible1, tps1, tpsOld1, erreur1, erreurOld1, integrale1, integraleOld1, derivee1, precision, ticks, 1, 1); // Asservissement en position du moteur 1
  ISR_asserv_PID(cod2Theta, cod2ThetaOld, Kp2_theta, Ki2_theta, Kd2_theta, RPMCible2, tps2, tpsOld2, erreur2, erreurOld2, integrale2, integraleOld2, derivee2, precision, ticks, 2, 1);
  ISR_asserv_PID(cod3Theta, cod3ThetaOld, Kp3_theta, Ki3_theta, Kd3_theta, RPMCible3, tps3, tpsOld3, erreur3, erreurOld3, integrale3, integraleOld3, derivee3, precision, ticks, 3, 1);
}



// Clear des cibles
void clearCibles(){
  thetaCible1 = 0;
  thetaCible2 = 0;
  thetaCible3 = 0;
  RPMCible1 = 0;
  RPMCible2 = 0;
  RPMCible3 = 0;

  // Clear des valeurs du PID
  // erreur 
  erreur1 = 0;
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
  
  cod1.write(0);
  cod2.write(0);
  cod3.write(0);
}
