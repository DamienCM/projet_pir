// Positions réelles
long cod1Theta = cod1.read();
long cod1ThetaOld = cod1.read();

long cod2Theta = cod2.read();
long cod2ThetaOld = cod2.read();

long cod3Theta = cod3.read();
long cod3ThetaOld = cod3.read();


// Coefficients des PID
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

// Temps
long tps1 = millis();
long tpsOld1 = 0;

long tps2 = millis();
long tpsOld2 = 0;

long tps3 = millis();
long tpsOld3 = 0;

// précision
const double precision = 2; //(en ticks)

// Ticks par tour
const double ticks = 660.0;
