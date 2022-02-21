// avr-libc library includes
#include <avr/io.h>
//******** Sine wave parameters ********
#define pi 3.1415 // 2*PI saves calculation later
int n=0;
int yint;
float fs,fa,Q,a,y,ym1,ym2;
float ymax, yscaled;
void setup()
{
 fs=8000;
 fa=200;
 Q=2*pi*fa/fs;
 a=2*cos(Q);
 y=0;
 ym1=1;
 //ym2=cos(Q);
 ym2=0;
 ymax=0;
 yscaled=0;
 yint=0;
DDRD = B11111111; // digital pins 7,6,5,4,3,2,1,0
}

void loop()
{
 y=a*ym1-ym2;
 ym2=ym1;
 ym1=y;
 if(ymax<y)
 {ymax=y;
 }
 n++;
 yscaled=(y/ymax+1)/2;
 yint=yscaled*255;
 yint=(int)yint;
 PORTD=yint;
}
