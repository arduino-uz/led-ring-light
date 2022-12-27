#include <EEPROM.h>

const int onOffPin = 2; // O'chirib yoqish tugmasi
const int modePin = 3; // Rejimni almashtirish tugmasi
const int upPin = 5; // Yorug'likni ko'tarish tugmasi
const int downPin = 4; // Yorug'likni pasaytirish tugmasi

const int ledF= 11; // PIN11 (interrupt)
const int ledS= 10; // PIN10 (interrupt)

const int maxBrightness= 10; // map funksiyasiga asoslanib 0-255gacha darajalarni chiqarish
const int brightnessInterval=1; // har bir daraja intervali

int onOffState = 0;
int mode = 1;
int brightness = maxBrightness;

unsigned long buttonMillis = 0;
unsigned long serialMillis = 0;

void setup() {
  Serial.begin(9600);

  // Pinlarni sozlash
  pinMode(onOffPin, INPUT_PULLUP);
  pinMode(modePin, INPUT_PULLUP);
  pinMode(upPin, INPUT_PULLUP);
  pinMode(downPin, INPUT_PULLUP);

  // EEPROM xotiradan konfiguratsiyalarni o'qish
  int c_onfstate, c_mode, c_brightness;
  c_onfstate = EEPROM.read(1);
  c_mode = EEPROM.read(2);
  c_brightness = EEPROM.read(3);

  // Joriy konfiguratsiyalarni moslash
  if(c_onfstate != 255){
    onOffState = c_onfstate;
  }
  if(c_mode != 255){
    mode = c_mode;
  }
  if(c_brightness != 255){
    brightness = c_brightness;
  }
}
void loop() {
  // Serial (kompyuter orqali kelgan ma'lumotlarni o'qish)
  if( Serial.available() > 0 ){
    int val = Serial.read();
    Serial.println(val);
    if ( val == 49 ) {
      onOffState = 1;
      EEPROM.write(1, 1);
    }
    if ( val == 50 ) {
      onOffState = 0;
      EEPROM.write(1, 0);
    }
    if ( val == 51 ) {
      mode = 1;
      EEPROM.write(2, 1);
    }
    if ( val == 52 ) {
      mode = 2;
      EEPROM.write(2, 2);
    }
    if ( val == 53 ) {
      mode = 3;
      EEPROM.write(2, 3);
    }
    if ( val == 54 && brightness < maxBrightness && onOffState) {
      brightness = brightness + brightnessInterval; 
      EEPROM.write(3, brightness);
    }
    if ( val == 55 && brightness > 0 && onOffState ) {
      brightness = brightness - brightnessInterval;
      EEPROM.write(3, brightness);
    }
  }

  // Tugma holatlarini kuzatish
  unsigned long currentMillis = millis();
  if(currentMillis - buttonMillis > 500){
    if (digitalRead(onOffPin) == LOW) {
      onOffState = !onOffState;
      EEPROM.write(1, onOffState);
      buttonMillis = currentMillis; 
    }
    if (digitalRead(modePin) == LOW && onOffState) {
      switch (mode) {
        case 1:
          mode = 2;
        break;
        case 2:
          mode = 3;
        break;
        case 3:
          mode = 1;
        break;
      }
      EEPROM.write(2, mode);
      buttonMillis = currentMillis; 
    }
    if (digitalRead(upPin) == LOW && brightness < maxBrightness && onOffState) {
      brightness = brightness + brightnessInterval;
      EEPROM.write(3, brightness);
      buttonMillis = currentMillis; 
    }
    if (digitalRead(downPin) == LOW && brightness > 0 && onOffState ) {
      brightness = brightness - brightnessInterval;
      EEPROM.write(3, brightness);
      buttonMillis = currentMillis; 
    }
  }

  // Tizimni ishga tushirish
  if(onOffState){
    if(mode  1 || mode  3){
      analogWrite(ledF, map(brightness, 0, maxBrightness, 0, 255));      
    }else{
      digitalWrite(ledF, LOW);
   }
    if(mode  2 || mode  3){
      analogWrite(ledS, map(brightness, 0, maxBrightness, 0, 255));      
    }else{
      digitalWrite(ledS, LOW);  
    }
  }else{
    digitalWrite(ledF, LOW);
    digitalWrite(ledS, LOW);  
  }
  
  // Agarda kompyuter bilan sinxronizatsiya qilish kerak bo'lsa o'zgaruvchilarni kompyuterga yuborish
  if (currentMillis - serialMillis >= 300) {
    serialMillis = currentMillis;
    Serial.println( String( onOffState)  + '|' + String(mode) + '|' + String(brightness ) );
  }

  // Jarayonni stabillashtirish
  delay(10);
}