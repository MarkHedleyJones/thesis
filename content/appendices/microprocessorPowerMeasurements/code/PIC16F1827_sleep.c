#include <htc.h>

__CONFIG(FOSC_INTOSC & WDTE_OFF & MCLRE_OFF & PWRTE_OFF
	& BOREN_OFF & FCMEN_OFF & IESO_OFF & CLKOUTEN_OFF
	& CP_OFF & CPD_OFF & LVP_ON & BORV_19 & STVREN_ON
	& PLLEN_OFF & WRT_OFF);


void main(void)
{
	//Set system clock to Internal osc block
    SCS0 = 0;
    SCS1 = 1;

	//Set internal osc freq = 31kHz
    IRCF3 = 0;
    IRCF2 = 0;
    IRCF1 = 0;
    IRCF0 = 0;

	//Disable interrupts
    GIE = 0;
    
    //Set all pins high (Tied to VDD via 10k)
    PORTA = 0xFF;
    PORTB = 0xFF;

	//Put to sleep
    SLEEP();
    while(1)
    {

    }   
}
