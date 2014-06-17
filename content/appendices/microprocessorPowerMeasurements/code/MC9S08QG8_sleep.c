#include <hidef.h> /* for EnableInterrupts macro */
#include "derivative.h" /* include peripheral declarations */

void main(void) {


  SOPT1 = 0b00100000;
  //        |||   ||
  //        |||   |\- RESET Pin Enable (0)
  //        |||   \-- Background Debug Mode Pin Enable (1)
  //        ||\------ Stop Mode Enable (0)
  //        |\------- COP Watchdog Timeout (1)
  //        \-------- COP Watchdog Enable (1)
    
  //Enable low power bit
  ICSC2 = 0b01001000;
  
  //Disable Low Voltage Detect
  SPMSC1 = 0x00;
  
  //Enable power down control
  //Disable partial power down
  SPMSC2 = 0x02;
  
  for(;;)
  {
    //Enter sleep mode
    _Stop;
  }
}