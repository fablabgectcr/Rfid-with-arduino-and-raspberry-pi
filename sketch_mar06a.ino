#include<ESP8266WiFi.h>
#include<ESP8266WebServer.h>
char * ssid_ap="ESP8266_SSID";
char * password_ap="tenonezero";
const int trigP = 2;
const int echoP = 0;
long duration;
float distance;

IPAddress ip(192,168,11,4);
IPAddress gateway(192,168,11,1);
IPAddress subnet(255,255,255,0);
ESP8266WebServer server;


void setup() {
  pinMode(trigP, OUTPUT);
  pinMode(echoP, INPUT);
  WiFi.mode(WIFI_AP);
  WiFi.softAPConfig(ip,gateway,subnet);
  WiFi.softAP(ssid_ap,password_ap);
  Serial.begin(115200);
  Serial.println();
  Serial.print("IP Address: ");Serial.println(WiFi.localIP());
  server.on("/",handleIndex);
  server.on("/update",handleUpdate);
  
  server.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
   server.handleClient();
   digitalWrite(trigP, LOW);   // Makes trigPin low
delayMicroseconds(2);       // 2 micro second delay 

digitalWrite(trigP, HIGH);  // tigPin high
delayMicroseconds(10);      // trigPin high for 10 micro seconds
digitalWrite(trigP, LOW);   // trigPin low

duration = pulseIn(echoP, HIGH);   //Read echo pin, time in microseconds
       //Output distance on arduino serial monitor 
distance= duration*0.034/2;
Serial.println(distance);
delay(3000);
   server.handleClient();
   
}

void handleIndex()
{
  server.send(200,"text/plain",String(distance));
}

void handleUpdate()
{
  distance =server.arg("distance").toFloat();
  Serial.println(duration);
  server.send(200,"text/plain","Updated");
  
}
