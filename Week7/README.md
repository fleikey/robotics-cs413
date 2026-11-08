# Week 7 – Go-to-goal control

The "54" trajectory (the last two digits of the student ID) as a list of waypoints, driven with a go-to-goal controller in the simulator and on the real robot. The comparison and the discussion are in **[odometry_analysis.ipynb](odometry_analysis.ipynb)**.

## Files

| File | Description |
| --- | --- |
| `go_to_goal_sim.qrs` | Go-to-goal through the waypoints in the simulator; logs the odometry. |
| `go_to_goal_real.qrs` | The same program for the real robot. |
| `odometry_gtg_sim.txt` | Simulator log. One line per sample: `x,y,time` (cm, cm, ms). |
| `odometry_gtg_real.txt` | Real-robot log, same format. |
| `odometry_gtg_real_mirrored.txt` | A second real-robot log. |
| `odometry_analysis.ipynb` | Planned vs simulated vs real trajectory, sim-vs-real error and discussion. |
