# Week 4 – Line-following competition

Programs for the line-following race on the big track: one lap on the real robot as fast as possible, with one wheel at 100 % PWM.

## Files

| File | Description |
| --- | --- |
| `alongTheBigLine.qrs` | P control. |
| `alongTheBigLine_P_control.qrs` | P control with a lap timer. |
| `alongTheBigLine_PI_control.qrs` | Same as `_P_control` with a 5 ms loop; no integral term. |
| `alongTheBigLine_PD_control.qrs` | PD control with a lap timer. |
| `alongTheBigLine_PID_control.qrs` | Same as `_PI_control`. |
| `week4.qrs` | PD control ($k_p = 9.5$, $k_d = 2$) with a lap timer. |
| `week4_real.qrs` | Real-robot version: calibrated sensors, P control, lower speed. |
