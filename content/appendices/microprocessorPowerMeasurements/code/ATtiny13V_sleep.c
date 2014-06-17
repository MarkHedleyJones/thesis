#include <avr/io.h>

int main(void)
{
    //POWER REDUCTION TIPS:
	//  * Disable DWEN fuse
	//  * Disable BODLEVEL fuse
	
	//Disable interrups
    SREG = 0x00;

	//Set PortB as outputs
    DDRB = 0b00000000;

	//Disable analog comparitor
	ACSR = 0x80;

	//Disable digital input
	DIDR0 = 0xFF;

	//Disable ADC before sleep
	ADCSRA = 0x00;

	//Set GPIOs as high
    PORTB = 0xFF;

	//Sequence to disable brown-
	//out detect while sleeping
    MCUCR = 0b00110000;

    while(1)
	{
		asm("sleep");
	}
}
