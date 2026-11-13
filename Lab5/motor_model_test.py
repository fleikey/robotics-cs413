import sys
import time
import random
import math

class Program():
  __interpretation_started_timestamp__ = time.time() * 1000

  pi = 3.141592653589793
  P = None
  TL = None
  TR = None
  UL = None
  UR = None
  Ubat = None
  W = None
  batt = None
  buff = None
  dw = None
  flush = None
  kL = None
  kR = None
  m = None
  t = None
  t0 = None
  theta_l = None
  theta_r = None
  ts = None
  uL = None
  uR = None
  v = None
  w = None
  wa = None
  wn = None
  wp = None

  def execMain(self):

    
    script.removeFile("model_test_data.txt")
    
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
    script.writeToFile("model_test_data.txt", "2 0 0 0 " + str(self.theta_l) + " " + str(self.theta_r) + " " + str(self.t) + " " + str(self.batt) + "\n")
    
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
    self.W = 6
    self.P = 32
    self.Ubat = self.batt
    self.kL = 0.475
    self.kR = 0.405
    self.TL = 0.308
    self.TR = 0.320
    self.m = 0
    self.w = 0
    self.uL = 0
    self.uR = 0
    
    while self.t < 128000:
      self.t = (time.time() * 1000 - self.__interpretation_started_timestamp__) - self.t0
      self.ts = self.t / 1000
      self.m = math.floor(self.ts / 64)
      self.m = (self.m + 1 - abs(self.m - 1)) / 2
      self.w = self.W * (1 - 4 * abs(self.ts / self.P - math.floor(self.ts / self.P) - 0.5))
      self.dw = 4 * self.W / self.P * (1 - 2 * math.floor(2 * (self.ts / self.P - math.floor(self.ts / self.P))))
      self.wa = abs(self.w)
      self.wp = (self.w + self.wa) / 2
      self.wn = (self.wa - self.w) / 2
      self.UL = self.wp / (self.wa + 0.000001) * (0.04337 + 0.15028 * self.wp + 0.05096 * self.wp * self.wp) - self.wn / (self.wa + 0.000001) * (0.04569 + 0.14518 * self.wn + 0.05478 * self.wn * self.wn) + 0.11291 * self.dw
      self.UR = self.wp / (self.wa + 0.000001) * (0.05394 + 0.10290 * self.wp + 0.03988 * self.wp * self.wp) - self.wn / (self.wa + 0.000001) * (0.03445 + 0.11719 * self.wn + 0.03676 * self.wn * self.wn) + 0.10261 * self.dw
      self.uL = (1 - self.m) * 100 * self.UL / self.Ubat + self.m * 100 * self.kL * (self.w + self.TL * self.dw) / self.Ubat
      self.uR = (1 - self.m) * 100 * self.UR / self.Ubat + self.m * 100 * self.kR * (self.w + self.TR * self.dw) / self.Ubat
      self.uL = math.floor((abs(self.uL + 100) - abs(self.uL - 100)) / 2 + 0.5)
      self.uR = math.floor((abs(self.uR + 100) - abs(self.uR - 100)) / 2 + 0.5)
      brick.motor("M3").setPower(int(self.uR))
      
      brick.motor("M4").setPower(int(self.uL))
      
      self.theta_l = brick.encoder("E4").read()
      self.theta_r = brick.encoder("E3").read()
      self.buff = self.buff + str(4 + self.m) + " " + str(self.w) + " " + str(self.uL) + " " + str(self.uR) + " " + str(self.theta_l) + " " + str(self.theta_r) + " " + str(self.t) + " " + str(self.batt) + "\n"
      script.wait(5)
      
      if self.t - self.flush >= 1000:
        self.batt = brick.battery().readVoltage()
        script.writeToFile("model_test_data.txt", self.buff)
        
        self.buff = ""
        self.flush = self.t
    brick.motor("M3").powerOff()
    brick.motor("M4").powerOff()
    
    script.writeToFile("model_test_data.txt", self.buff)
    
    brick.stop()
    return

def main():
  program = Program()
  program.execMain()

if __name__ == '__main__':
  main()
