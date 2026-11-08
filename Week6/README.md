# Week 6 – Odometry localization

The "54" trajectory (the last two digits of the student ID) is driven by the same program in the simulator and on the real robot, and the two odometry logs are compared. The plots, the measured end point and the discussion are in **[odometry_analysis.ipynb](odometry_analysis.ipynb)**.

## Files

| File | Description |
| --- | --- |
| `trajectory_sim.qrs` | Drives the trajectory in the simulator and logs the odometry every 30 ms. |
| `trajectory_real.qrs` | The same program with the real robot's $r$ and $B$. |
| `odometry_data_sim.txt` | Simulator log. One line per sample: `x,y,time` (m, m, ms). |
| `odometry_data_real.txt` | Real-robot log, same format. |
| `odometry_analysis.ipynb` | Trajectory plot, sim-vs-real error, measured end point and discussion. |

## Results

| End point | x, m | y, m |
| --- | ---: | ---: |
| Simulator (odometry) | −0.270 | 0.270 |
| Real robot (odometry) | −0.720 | 0.694 |
| Real robot (tape) | −0.83 | 0.80 |

Sim vs real error: 0.618 m at the end, 0.664 m at most. Real odometry vs the tape: 0.152 m.
