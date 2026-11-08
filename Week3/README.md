# Week 3 – Line following

Line following on the V-shaped track with two line sensors. `V_shaped_unaware.qrs` is the correct running version. The most efficient version is plain PD control with a nonlinear speed term: the speed decreases as the error increases.

## Files

| File                   | Description                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------- |
| `V_shaped_unaware.qrs` | The working version: PD control, slowing down as the error grows.                  |
| `V_shaped_aware.qrs`   | Attempt with binary flags: whether each sensor sees dark, by a darkness threshold. |
| `video.mp4`            | The real robot on the V-shaped track.                                              |
