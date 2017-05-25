/*
  
 */

// include the library code:
#include <LiquidCrystal.h>

long int a=0,b,c;
// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup(){
    // set up the LCD's number of columns and rows: 
  lcd.begin(16, 2);
  // initialize the serial communications:
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  lcd.clear();
}

void loop()
{
  // when characters arrive over the serial port...
while(Serial.available()>0)
{
  if(a==0)
  {
  a=Serial.parseInt();
  if(a<=162)
  {
    b=a%10;
    c=a/10;
    if(b<=2 && c<=16)
    {
    lcd.setCursor((c-1),(b-1));
    }
    else{
      a=0;
    }
    Serial.flush();
  }
  else{
    a=0;
  }
  }
   if(a!=0){
     if((char)Serial.read()==' ')
     {
    lcd.print(Serial.readStringUntil('\n'));
     }
    a=0;
     
  }
  
}

}
