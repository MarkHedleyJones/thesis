LIST   P=PIC16F1827
#include <P16F1827.INC>

	__CONFIG _CONFIG1 , _FOSC_INTOSC & _WDTE_OFF & _PWRTE_OFF & _MCLRE_OFF & _CP_OFF & _CPD_OFF & _BOREN_OFF & _CLKOUTEN_OFF & _IESO_OFF & _FCMEN_OFF
	__CONFIG _CONFIG2 , _WRT_OFF & _PLLEN_OFF & _STVREN_OFF & _BORV_19 & _LVP_ON


ORG 0x0000 ; Specifies where to place the following code (which in this case is at the beginning of memory space )

START
	;Disable interrupts
	BANKSEL INTCON
	CLRF INTCON
	;Disable watchdog
	BANKSEL WDTCON
	CLRF WDTCON
	;Disable capacitive sensing
	BANKSEL CPSCON0
	CLRF CPSCON0
	;Disable modulation control
	BANKSEL MDCON
	CLRF MDCON
	;Disable perhiperal interrupts
	BANKSEL PIE1
	CLRF PIE2
	;Disable timer 1
	BANKSEL T1CON
	CLRF T1CON
	;Disable DAC
	BANKSEL DACCON0
	CLRF DACCON0
	;Disable ADC
	BANKSEL ADCON0
	CLRF ADCON0
	BANKSEL ADCON1
	CLRF ADCON1
	;Disable timers
	BANKSEL T2CON
	CLRF T2CON
	BANKSEL T4CON
	CLRF T4CON
	BANKSEL T6CON
	CLRF T6CON
	;Init PortA
	BANKSEL PORTA ;
	CLRF PORTA ;Init PORTA
	BANKSEL LATA ;Data Latch
	CLRF LATA ;
	COMF LATA ;
	BANKSEL ANSELA ;
	CLRF ANSELA ;digital I/O
	BANKSEL TRISA ;
	CLRF TRISA ;SET AS OUTPUT
	;Init PortB
	BANKSEL PORTB ;
	CLRF PORTB ;Init PORTB
	BANKSEL LATB
	CLRF LATB ;
	COMF LATB ;
	BANKSEL ANSELB
	CLRF ANSELB ;Make RB<7:0> digital
	BANKSEL TRISB ;
	;and RB<3:0> as outputs
	CLRF TRISB ;

LOOP ; Label this position (forms the start of a loop)
	SLEEP
	GOTO LOOP
END
