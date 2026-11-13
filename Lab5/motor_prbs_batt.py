import sys
import time
import random
import math

class Program():
  __interpretation_started_timestamp__ = time.time() * 1000

  pi = 3.141592653589793
  A = None
  T = None
  Tc = None
  b5 = None
  b6 = None
  batt = None
  buff = None
  f0 = None
  f1 = None
  flush = None
  k = None
  k_last = None
  nb = None
  r = None
  rn = None
  s = None
  t = None
  t0 = None
  theta_l = None
  theta_r = None
  ts = None
  v = None

  def execMain(self):

    
    script.removeFile("prbs_signal_data.txt")
    
    self.t0 = (time.time() * 1000 - self.__interpretation_started_timestamp__)
    self.batt = brick.battery().readVoltage()                # battery read (was `batt =`, then reset to 0)
    self.t = 0
    brick.encoder("E3").reset()
    brick.encoder("E4").reset()
    
    brick.motor("M3").setPower(0)
    brick.motor("M4").setPower(0)
    
    script.wait(3000)
    
    self.theta_l = brick.encoder("E4").read()
    self.theta_r = brick.encoder("E3").read()
    self.t = (time.time() * 1000 - self.__interpretation_started_timestamp__) - self.t0
    script.writeToFile("prbs_signal_data.txt", "2 " + "0" + " " + str(self.theta_l) + " " + str(self.theta_r) + " " + str(self.t) + " " + str(self.batt) + "\n")
    
    brick.encoder("E3").reset()
    brick.encoder("E4").reset()
    
    self.t0 = (time.time() * 1000 - self.__interpretation_started_timestamp__)
    self.t = 0
    self.v = -100
    self.batt = brick.battery().readVoltage()                # battery read, so the first second is not 0
    self.flush = self.t
    self.theta_l = brick.encoder("E4").read()
    self.theta_r = brick.encoder("E3").read()
    self.buff = ""
    self.A = 20
    self.Tc = 0.5
    self.r = 1
    self.k_last = 0
    self.f0 = 0.1
    self.f1 = 5
    self.T = 30
    
    while self.t < 127000:
      self.t = (time.time() * 1000 - self.__interpretation_started_timestamp__) - self.t0
      self.ts = self.t / 1000
      self.k = math.floor(self.ts / self.Tc)
      self.s = self.k - self.k_last
      self.b6 = math.floor(self.r / 64)
      self.b5 = math.floor(self.r / 32) - 2 * self.b6
      self.nb = self.b6 + self.b5 - 2 * math.floor((self.b6 + self.b5) / 2)
      self.rn = 2 * self.r + self.nb - 128 * math.floor((2 * self.r + self.nb) / 128)
      self.r = self.s * self.rn + (1 - self.s) * self.r
      self.k_last = self.k
      self.v = self.A * (2 * (self.r - 2 * math.floor(self.r / 2)) - 1)
      brick.motor("M3").setPower(self.v)
      
      brick.motor("M4").setPower(self.v)
      
      self.theta_l = brick.encoder("E4").read()
      self.theta_r = brick.encoder("E3").read()
      self.buff = self.buff + "3 " + str(self.v) + " " + str(self.theta_l) + " " + str(self.theta_r) + " " + str(self.t) + " " + str(self.batt) + "\n"
      script.wait(5)
      
      if self.t - self.flush >= 1000:
        self.batt = brick.battery().readVoltage()            # was `batt =`: a local variable, never logged
        script.writeToFile("prbs_signal_data.txt", self.buff)
        
        self.buff = ""
        self.flush = self.t
    brick.motor("M3").powerOff()
    brick.motor("M4").powerOff()
    
    script.writeToFile("prbs_signal_data.txt", self.buff)
    
    brick.stop()
    return

def main():
  program = Program()
  program.execMain()

if __name__ == '__main__':
  main()
