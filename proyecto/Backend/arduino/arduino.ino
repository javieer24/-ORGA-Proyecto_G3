#include <Stepper.h>

const int stepsPerRevolution = 300; // Assuming both motors have the same steps per revolution

// motores stepper
Stepper motor1(stepsPerRevolution, 4, 5, 6, 7);
Stepper motor2(stepsPerRevolution, 8, 9, 10, 11);

// pines para escribir en memoria
const int bit0 = 22;
const int bit1 = 23;
const int bit2 = 24;
const int bit3 = 25;
const int bit4 = 26;
// pines para elegir el registro
const int pos0 = 28;
const int pos1 = 29;
const int pos2 = 30;
const int pos3 = 31;
// pines para leer la ram
const int read0 = 32;
const int read1 = 33;
const int read2 = 34;
const int read3 = 35;
const int read4 = 36;
// alternar escritura y lectura
const int wr = 13;

// variables para determinar la posicion del brazo
int posmatriz = 0;
int ciclo = 0;

void setup() {
 Serial1.begin(9600);
 pinMode(bit0, OUTPUT);
 pinMode(bit1, OUTPUT);
 pinMode(bit2, OUTPUT);
 pinMode(bit3, OUTPUT);
 pinMode(bit4, OUTPUT);
 pinMode(pos0, OUTPUT);
 pinMode(pos1, OUTPUT);
 pinMode(pos2, OUTPUT);
 pinMode(pos3, OUTPUT);
 pinMode(read0, INPUT);
 pinMode(read1, INPUT);
 pinMode(read2, INPUT);
 pinMode(read3, INPUT);
 pinMode(read4, INPUT);
 pinMode(wr, OUTPUT);
}

void loop() {
  // variables para guardar el mensaje
  static char figura[5];
  static unsigned int pos = 0;

  // elegir la ram
  static unsigned int numreg = 0;


  static unsigned int mempos = -1;
  ciclo = 0;

  // modo escritura
  digitalWrite(wr, HIGH);

 // revisar si hay algo en el buffer
  if (Serial1.available() > 0)
  {
   // guardando un bit
   char bit = Serial1.read();
  
   // a;adir bit a la cadena
   if (bit != 'b')
   {
     figura[pos] = bit;
     pos++;
   }else{
     pos = 0;
     mempos++;
     // posicion en el registro
    numreg = mempos % 4;
    ciclo = int(mempos / 4);
    if(numreg == 0){
      digitalWrite(pos0, HIGH);
      digitalWrite(pos1, LOW);
      digitalWrite(pos2, LOW);
      digitalWrite(pos3, LOW);
    }
    if(numreg == 1){
      digitalWrite(pos0, LOW);
      digitalWrite(pos1, HIGH);
      digitalWrite(pos2, LOW);
      digitalWrite(pos3, LOW);
    }

    if(numreg == 2){
      digitalWrite(pos0, LOW);
      digitalWrite(pos1, LOW);
      digitalWrite(pos2, HIGH);
      digitalWrite(pos3, LOW);
    }

    if(numreg == 3){
      digitalWrite(pos0, LOW);
      digitalWrite(pos1, LOW);
      digitalWrite(pos2, LOW);
      digitalWrite(pos3, HIGH);
      // Ejecutar impresion con la memoria actual
      //lectura();
    }

    // guardar en memoria la cadena
    if(figura[0] =='1'){
        digitalWrite(bit0, HIGH);
     }
     else{
        digitalWrite(bit0, LOW);
     }

     if(figura[1] =='1'){
        digitalWrite(bit1, HIGH);
     }
     else{
        digitalWrite(bit1, LOW);
     }

     if(figura[2] =='1'){
        digitalWrite(bit2, HIGH);
     }
     else{
        digitalWrite(bit2, LOW);
     }

     if(figura[3] =='1'){
        digitalWrite(bit3, HIGH);
     }
     else{
        digitalWrite(bit3, LOW);
     }

     if(figura[4] =='1'){
        digitalWrite(bit4, HIGH);
     }
     else{
        digitalWrite(bit4, LOW);
     }
     posicion(mempos);
   }
    
 }
}

void lectura(){
      // posicion inicial en matriz
      static unsigned int posmatriz = ciclo * 4;

      // leer la ram
      digitalWrite(wr, LOW);
      delay(100);

      // primer reg
      digitalWrite(pos0, HIGH);
      digitalWrite(pos1, LOW);
      digitalWrite(pos2, LOW);
      digitalWrite(pos3, LOW);


      // cambiar la posicion
      posmatriz += 1;
      // segundo reg
      digitalWrite(pos0, LOW);
      digitalWrite(pos1, HIGH);
      digitalWrite(pos2, LOW);
      digitalWrite(pos3, LOW);


      // cambiar la posicion
      posmatriz += 1;
      // tercer reg
      digitalWrite(pos0, LOW);
      digitalWrite(pos1, LOW);
      digitalWrite(pos2, HIGH);
      digitalWrite(pos3, LOW);

      // cambiar la posicion
      posmatriz += 1;
      // cuarto reg
      digitalWrite(pos0, LOW);
      digitalWrite(pos1, LOW);
      digitalWrite(pos2, LOW);
      digitalWrite(pos3, HIGH);
      //delay(10000);
}

// coloca el lapiz en la posicion que le corresponde
void posicion(int m){
  if(m == 0){
    // posicion inicial
    izquierda();
    izquierda();
    arriba();
    arriba();
  }
  if(m == 1){
    derecha();
  }
  if(m == 2){
    derecha();
  }
  if(m == 3){
    izquierda();
    izquierda();
    abajo();
  }
  if(m == 4){
    derecha();
  }
  if(m == 5){
    derecha();
  }
  if(m == 6){
    izquierda();
    izquierda();
    abajo();
  }
  if(m == 7){
    derecha();
  }
  if(m == 8){
    derecha();
  }
  delay(3000);
}

// lee de la ram el binario y genera la respectiva figura
void figura(){
  static unsigned int r0 = digitalRead(read0);
  static unsigned int r1 = digitalRead(read1);
  static unsigned int r2 = digitalRead(read2);
  static unsigned int r3 = digitalRead(read3);
  static unsigned int r4 = digitalRead(read4);

  // vacio
  if(r0 == LOW && r1 == LOW && r2 == LOW && r3 == LOW && r4 == LOW){
  }
  // estrella cyan
  if(r0 == LOW && r1 == LOW && r2 == LOW && r3 == LOW && r4 == HIGH){
    cyan();
    estrella();
  }
  // estrella magenta
  if(r0 == LOW && r1 == LOW && r2 == LOW && r3 == HIGH && r4 == HIGH){
    magenta();
    estrella();
  }
  // estrella amarilla
  if(r0 == LOW && r1 == LOW && r2 == HIGH && r3 == LOW && r4 == HIGH){
    amarillo();
    estrella();
  }
  // estrella negra
  if(r0 == LOW && r1 == LOW && r2 == HIGH && r3 == HIGH && r4 == HIGH){
    negro();
    estrella();
  }
  // equis cyan
  if(r0 == LOW && r1 == HIGH && r2 == LOW && r3 == LOW && r4 == HIGH){
    cyan();
    equis();
  }
  // equis magenta
  if(r0 == LOW && r1 == HIGH && r2 == LOW && r3 == HIGH && r4 == HIGH){
    magenta();
    equis();
  }
  // equis amarilla
  if(r0 == LOW && r1 == HIGH && r2 == HIGH && r3 == LOW && r4 == HIGH){
    amarillo();
    equis();
  }
  // equis negra
  if(r0 == LOW && r1 == HIGH && r2 == HIGH && r3 == HIGH && r4 == HIGH){
    negro();
    equis();
  }
  // circulo cyan
  if(r0 == HIGH && r1 == LOW && r2 == LOW && r3 == LOW && r4 == HIGH){
    cyan();
    circulo();

  }
  // circulo magenta
  if(r0 == HIGH && r1 == LOW && r2 == LOW && r3 == HIGH && r4 == HIGH){
    magenta();
    circulo();
  }
  // circulo amarillo
  if(r0 == HIGH && r1 == LOW && r2 == HIGH && r3 == LOW && r4 == HIGH){
    amarillo();
    circulo();
  }
  // circulo negro
  if(r0 == HIGH && r1 == LOW && r2 == HIGH && r3 == HIGH && r4 == HIGH){
    negro();
    circulo();
  }
  // triangulo cyan
  if(r0 == HIGH && r1 == HIGH && r2 == LOW && r3 == LOW && r4 == HIGH){
    cyan();
    triangulo();
  }
  // triangulo magenta
  if(r0 == HIGH && r1 == HIGH && r2 == LOW && r3 == HIGH && r4 == HIGH){
    magenta();
    triangulo();
  }
  // triangulo amarillo
  if(r0 == HIGH && r1 == HIGH && r2 == HIGH && r3 == LOW && r4 == HIGH){
    amarillo();
    triangulo();
  }
  // triangulo negro
  if(r0 == HIGH && r1 == HIGH && r2 == HIGH && r3 == HIGH && r4 == HIGH){
    negro();
    triangulo();
  }
}

// MOVIMIENTOS DEL MOTOR
// movimiento del stepper
void derecha(){
  motor1.setSpeed(10);
  motor1.step(100);
}

void izquierda(){
  motor1.setSpeed(10);
  motor1.step(-100);
}

void arriba(){
  motor2.setSpeed(10);
  motor2.step(100);
}

void abajo(){
  motor2.setSpeed(10);
  motor2.step(-100);
}

// funciones de color
void amarillo(){
  // led?
}

void cyan(){
  // led?
}

void magenta(){
  // led?
}

void negro(){
  // led?
}


// funciones de figura
void circulo(){
  static unsigned int x = 0;
  static unsigned int y = 0;
  // x = 0 a 2pi
  //  = rsen(x)
  // x' = rcos(a)
  // y = rsen(a)
  // y' = -rsen(a)
  // pos inicial
  motor1.setSpeed(10);
  motor1.step(50);
  

}

void triangulo(){
  motor2.setSpeed(10);
  motor2.step(50);
  // activar servo
  for(int i = 0; i < 25; i++){
    motor1.setSpeed(4);
    motor1.step(2);
    motor2.setSpeed(4);
    motor2.step(-4);
  }

  izquierda();

  for(int i = 0; i < 25; i++){
    motor1.setSpeed(4);
    motor1.step(2);
    motor2.setSpeed(4);
    motor2.step(4);
  }

  // desactivar servo
  motor2.setSpeed(10);
  motor2.step(-50);

}

void estrella(){
  equis();
  // desactivar servo 
  motor2.setSpeed(10);
  motor2.step(50);
  // activar servo
  derecha();
  // desactivar servo 
  motor2.setSpeed(10);
  motor2.step(-50);
  motor1.setSpeed(10);
  motor1.step(-50);
  // activar servo
  abajo();

}

void equis(){
  // activar servo
  for(int i = 0; i < 25; i++){
    motor1.setSpeed(4);
    motor1.step(4);
    motor2.setSpeed(4);
    motor2.step(-4);
  }
  
  // desactivar servo 
  arriba();

  // activar servo
  for(int i = 0; i < 25; i++){
    motor1.setSpeed(4);
    motor1.step(-4);
    motor2.setSpeed(4);
    motor2.step(-4);
  }

  // desactivar servo 
  arriba();
}