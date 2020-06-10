int trigPin1=3;
int trigPin2=5;
int trigPin3=7;
int trigPin4=9;

int echoPin1=2;
int echoPin2=4;
int echoPin3=6;
int echoPin4=8;

int buzzer=13;

int distance[4];
long duration[4];

void setup() {
  
  pinMode(trigPin1, OUTPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(trigPin3, OUTPUT);
  pinMode(trigPin4, OUTPUT);

  pinMode(echoPin1, INPUT);
  pinMode(echoPin2, INPUT);
  pinMode(echoPin3, INPUT);
  pinMode(echoPin4, INPUT);

  pinMode(buzzer, OUTPUT);

}

void sensor(){
  
  digitalWrite(3, HIGH);
  digitalWrite(5, HIGH);
  digitalWrite(7, HIGH);
  digitalWrite(9, HIGH);
  
  delay(1000);
  
  digitalWrite(3, LOW);
  digitalWrite(5, LOW);
  digitalWrite(7, LOW);
  digitalWrite(9, LOW);
 
}




void take(){

duration[0]=pulseIn(2,HIGH);
distance[0]=((duration[0]*0.034)/2);

duration[1]=pulseIn(4,HIGH);
distance[1]=((duration[0]*0.034)/2);

duration[2]=pulseIn(6,HIGH);
distance[2]=((duration[0]*0.034)/2);

duration[3]=pulseIn(8,HIGH);
distance[3]=((duration[0]*0.034)/2);

}


void buzz()
{
   for(int i=0;i<4;i++){

    if(distance[i]<10){
      
      tone(buzzer,1000);
    }
    else{
      noTone(buzzer);
    }
  }

}

void loop() {

  sensor();
  take();
  buzz();

}
