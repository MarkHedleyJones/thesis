#include <htc.h>

__CONFIG(FOSC_INTOSC & WDTE_OFF & MCLRE_OFF & PWRTE_OFF
	& BOREN_OFF & FCMEN_OFF & IESO_OFF & CLKOUTEN_OFF
	& CP_OFF & CPD_OFF & LVP_ON & BORV_19 & STVREN_ON
	& PLLEN_ON & WRT_OFF);

unsigned int count;

void main(void)
{
	//Set system clock to Internal osc block
    SCS0 = 0;
    SCS1 = 0;

	//Set internal osc freq = 31kHz
    IRCF3 = 1;
    IRCF2 = 1;
    IRCF1 = 1;
    IRCF0 = 0;

	//Disable interrupts
    GIE = 0;
    
    //Disable serial ports
    SSP1CON1 = 0x00;
    SSP2CON1 = 0x00;
    
    ADCON0 = 0x00;
    
    //Disable modulation
    MDSRC = 0b10000000;
    MDCARH = 0b10000000;
    MDCARL = 0b10000000;
    
    //Add pins as outputs
    TRISA = 0x00;
    ANSELA = 0x00;
    TRISB = 0x00;
    ANSELB = 0x00;
    
    //Set all pins high (Tied to VDD via 10k)
    PORTA = 0xFF;
    PORTB = 0xFF;

	//Put to sleep
    while(1)
    {
	    count++;
    }   
}