import sys
import time
import random
import math

class Program():
  __interpretation_started_timestamp__ = time.time() * 1000

  pi = 3.141592653589793
  A = None
  N = None
  P = None
  batt = None
  buff = None
  flush = None
  t = None
  t0 = None
  theta_l = None
  theta_r = None
  ts = None
  v = None

  def execMain(self):

    
    script.removeFile("triangle_signal_data.txt")
    
    self.t0 = (time.time() * 1000 - self.__interpretation_started_timestamp__)
    self.batt = brick.battery().readVoltage()
    self.t = 0
    brick.encoder("E3").reset()
    brick.encoder("E4").reset()
    
    brick.motor("M3").setPower(0)
    brick.motor("M4").setPower(0)
    
    script.wait(3000)
    
    self.theta_l = brick.encoder("E4").read()
    self.theta_r = brick.encoder("E3").read()
    self.t = (time.time() * 1000 - self.__interpretation_started_timestamp__) - self.t0
    script.writeToFile("triangle_signal_data.txt", "2 " + "0" + " " + str(self.theta_l) + " " + str(self.theta_r) + " " + str(self.t) + " " + str(self.batt) + "\n")
    
    brick.encoder("E3").reset()
    brick.encoder("E4").reset()
    
    self.t0 = (time.time() * 1000 - self.__interpretation_started_timestamp__)
    self.t = 0
    self.v = -100
    self.batt = brick.battery().readVoltage()
    self.flush = self.t
    self.theta_l = brick.encoder("E4").read()
    self.theta_r = brick.encoder("E3").read()
    self.buff = ""
    self.A = 40
    self.P = 32
    self.N = 5
    
    while self.t < self.N * 32000:
      self.t = (time.time() * 1000 - self.__interpretation_started_timestamp__) - self.t0
      self.ts = self.t / 1000
      self.v = self.A * (1 - 4 * abs(self.ts / self.P - math.floor(self.ts / self.P) - 0.5))
      brick.motor("M3").setPower(int(self.v))
      
      brick.motor("M4").setPower(int(self.v))
      
      self.theta_l = brick.encoder("E4").read()
      self.theta_r = brick.encoder("E3").read()
      self.buff = self.buff + "3 " + str(self.v) + " " + str(self.theta_l) + " " + str(self.theta_r) + " " + str(self.t) + " " + str(self.batt) + "\n"
      script.wait(5)
      
      if self.t - self.flush >= 1000:
        self.batt = brick.battery().readVoltage()
        script.writeToFile("triangle_signal_data.txt", self.buff)
        
        self.buff = ""
        self.flush = self.t
    brick.motor("M3").powerOff()
    brick.motor("M4").powerOff()
    
    script.writeToFile("triangle_signal_data.txt", self.buff)
    
    brick.stop()
    return

def main():
  program = Program()
  program.execMain()

if __name__ == '__main__':
  main()
