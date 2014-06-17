#include <avr/io.h>

int main(void)
{
    unsigned char rand;
    SREG = 0x00;
	//Set PortB as outputs
    DDRB = 0b11111111;
	//Set pins high
    PORTB = 0xFF;
    for(;;)
    {
        rand++;
        asm("nop");
    }

}
