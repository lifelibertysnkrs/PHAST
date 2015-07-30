/*
Developed at NASA Goddard
 */

// pins for the LEDs:
const int input = 3;
input motor = 7;
int pos = 0;    // variable to store the servo position 

void setup() {
  // initialize serial:
  Serial.begin(9600);
  // make the pins outputs:
  pinMode(input, OUTPUT);

  Servo myservo;  // create servo object to control a servo 
                
 
  
  int increment = 15; //degrees to adjust focus by

}

void loop() {
  // if there's any serial available, read it:
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object 
  while (Serial.available() > 0) {

    // look for the next valid integer in the incoming serial stream:
    int input = Serial.parseInt();

    if (input == '0') {
      pos = 0
      myservo.write(pos);              // tell servo to go to position in variable 'pos' 
      delay(1000)
    }

    if (input == '1'){
      pos+= increment;
      myservo.write(pos);
      delay(1000)
    }
      
       
} 

  

}
  




