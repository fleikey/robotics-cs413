import sys
import time
import random
import math

class Program():
  __interpretation_started_timestamp__ = time.time() * 1000

  pi = 3.141592653589793
  A = None
  T = None
  batt = None
  buff = None
  f0 = None
  f1 = None
  flush = None
  t = None
  t0 = None
  theta_l = None
  theta_r = None
  ts = None
  v = None
  u= None

  def execMain(self):

    
    script.removeFile("signal_data.txt")
    
    self.t0 = (time.time() * 1000 - self.__interpretation_started_timestamp__)
    self.t = 0
    self.batt = brick.battery().readVoltage()
    brick.encoder("E3").reset()
    brick.encoder("E4").reset()
    
    brick.motor("M3").setPower(0)
    brick.motor("M4").setPower(0)
    
    script.wait(3000)
    
    self.theta_l = brick.encoder("E4").read()
    self.theta_r = brick.encoder("E3").read()
    self.t = (time.time() * 1000 - self.__interpretation_started_timestamp__) - self.t0
    script.writeToFile("signal_data.txt", "2 " + "0" + " " + str(self.theta_l) + " " + str(self.theta_r) + " " + str(self.t) + " " + str(self.batt) + "\n")
    
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
    self.A = 80
    self.f0 = 0.1
    self.f1 = 5
    self.T = 30
    
    while self.t < 30000:
      self.t = (time.time() * 1000 - self.__interpretation_started_timestamp__) - self.t0
      self.ts = self.t / 1000
      self.v = self.A * math.sin(2 * self.pi * (self.f0 * self.ts + (self.f1 - self.f0) * self.ts * self.ts / (2 * self.T)))
      
      self.u = int(self.v)
      brick.motor("M3").setPower(self.u)
      brick.motor("M4").setPower(self.u)
      
      self.theta_l = brick.encoder("E4").read()
      self.theta_r = brick.encoder("E3").read()
      self.buff = self.buff + "3 " + str(self.u) + " " + str(self.theta_l) + " " + str(self.theta_r) + " " + str(self.t) + " " + str(self.batt) + "\n"
      script.wait(5)
      
      if self.t - self.flush >= 1000:
        self.batt = brick.battery().readVoltage()
        script.writeToFile("signal_data.txt", self.buff)
        
        self.buff = ""
        self.flush = self.t
    brick.motor("M3").powerOff()
    brick.motor("M4").powerOff()
    
    script.writeToFile("signal_data.txt", self.buff)
    
    brick.stop()
    return

def main():
  program = Program()
  program.execMain()

if __name__ == '__main__':
  main()
