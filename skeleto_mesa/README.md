``` [RaspberryPI] <ethernet> [7i92] <db25> [blue china bob] <IO> [Step drivers] & spindle & inputs```


DIR     TASK        BOBPin     MesaPort         MesaIO  Chan
        PWM         P1          P1              17      1
        X STEP      P2          P1              19      4
        X DIR       P3          P1              21
        Y STEP      P4          P1              23      5
        Y DIR       P5          P1              25
        Z STEP      P6          P1              26      6
        Z DIR       P7          P1              27
        A STEP      P8          P1              28
        A DIR       P9          P1              29
        ESTOP       P10         P1              30
        TOUCH       P11         P1              31
        X HOME      P12         P1              32
        Y HOME      P13         P1              33
        ENABLE      P14         P1              18
        Z HOME      P15         P1              20
        B STEP(CW)  P16         P1              22
        B DIR(RELAY)P17         P1              24

        GROUND      P18         P1
        GROUND      P19         P1
        GROUND      P20         P1
        GROUND      P21         P1
        GROUND      P22         P1
        GROUND      P23         P1
        GROUND      P24         P1
        GROUND      P25         P1
        

hm2_eth: 10.10.10.10: INFO: Hardware address (MAC): 00:60:1b:13:05:f7
hm2_eth: discovered 7I92
hm2/hm2_7i92.0: Low Level init 0.15
hm2/hm2_7i92.0: 34 I/O Pins used:
hm2/hm2_7i92.0:     IO Pin 000 (P2-01): PWMGen #0, pin Out0 (PWM or Up) (Output)
hm2/hm2_7i92.0:     IO Pin 001 (P2-14): IOPort
hm2/hm2_7i92.0:     IO Pin 002 (P2-02): StepGen #0, pin Step (Output)
hm2/hm2_7i92.0:     IO Pin 003 (P2-15): IOPort
hm2/hm2_7i92.0:     IO Pin 004 (P2-03): StepGen #0, pin Direction (Output)
hm2/hm2_7i92.0:     IO Pin 005 (P2-16): IOPort
hm2/hm2_7i92.0:     IO Pin 006 (P2-04): StepGen #1, pin Step (Output)
hm2/hm2_7i92.0:     IO Pin 007 (P2-17): IOPort
hm2/hm2_7i92.0:     IO Pin 008 (P2-05): StepGen #1, pin Direction (Output)
hm2/hm2_7i92.0:     IO Pin 009 (P2-06): StepGen #2, pin Step (Output)
hm2/hm2_7i92.0:     IO Pin 010 (P2-07): StepGen #2, pin Direction (Output)
hm2/hm2_7i92.0:     IO Pin 011 (P2-08): StepGen #3, pin Step (Output)
hm2/hm2_7i92.0:     IO Pin 012 (P2-09): StepGen #3, pin Direction (Output)
hm2/hm2_7i92.0:     IO Pin 013 (P2-10): IOPort
hm2/hm2_7i92.0:     IO Pin 014 (P2-11): IOPort
hm2/hm2_7i92.0:     IO Pin 015 (P2-12): IOPort
hm2/hm2_7i92.0:     IO Pin 016 (P2-13): IOPort

hm2/hm2_7i92.0:     IO Pin 017 (P1-01): PWMGen #1, pin Out0 (PWM or Up) (Output)
hm2/hm2_7i92.0:     IO Pin 018 (P1-14): IOPort
hm2/hm2_7i92.0:     IO Pin 019 (P1-02): StepGen #4, pin Step (Output)
hm2/hm2_7i92.0:     IO Pin 020 (P1-15): IOPort
hm2/hm2_7i92.0:     IO Pin 021 (P1-03): StepGen #4, pin Direction (Output)
hm2/hm2_7i92.0:     IO Pin 022 (P1-16): IOPort
hm2/hm2_7i92.0:     IO Pin 023 (P1-04): StepGen #5, pin Step (Output)
hm2/hm2_7i92.0:     IO Pin 024 (P1-17): IOPort
hm2/hm2_7i92.0:     IO Pin 025 (P1-05): StepGen #5, pin Direction (Output)
hm2/hm2_7i92.0:     IO Pin 026 (P1-06): StepGen #6, pin Step (Output)
hm2/hm2_7i92.0:     IO Pin 027 (P1-07): StepGen #6, pin Direction (Output)
hm2/hm2_7i92.0:     IO Pin 028 (P1-08): StepGen #7, pin Step (Output)
hm2/hm2_7i92.0:     IO Pin 029 (P1-09): StepGen #7, pin Direction (Output)
hm2/hm2_7i92.0:     IO Pin 030 (P1-10): IOPort
hm2/hm2_7i92.0:     IO Pin 031 (P1-11): IOPort
hm2/hm2_7i92.0:     IO Pin 032 (P1-12): IOPort
hm2/hm2_7i92.0:     IO Pin 033 (P1-13): IOPort
hm2/hm2_7i92.0: registered