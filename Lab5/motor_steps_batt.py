import sys
import time
import random
import math

class Program():
  __interpretation_started_timestamp__ = time.time() * 1000

  pi = 3.141592653589793
  batt = None
  buff = None
  t = None
  t0 = None
  theta_l = None
  theta_r = None
  v = None

  def execMain(self):

    
    script.removeFile("trik_steps.txt")
    
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
    script.writeToFile("trik_steps.txt", "2 " + "0" + " " + str(self.theta_l) + " " + str(self.theta_r) + " " + str(self.t) + " " + str(self.batt) + "\n")
    
    self.t0 = (time.time() * 1000 - self.__interpretation_started_timestamp__)
    self.t = 0
    self.v = -100
    self.batt = brick.battery().readVoltage()
    self.theta_l = brick.encoder("E4").read()
    self.theta_r = brick.encoder("E3").read()
    
    while self.v <= 100:
      brick.encoder("E3").reset()
      brick.encoder("E4").reset()
      
      self.t0 = (time.time() * 1000 - self.__interpretation_started_timestamp__)
      self.t = 0
      self.buff = ""
      brick.motor("M3").setPower(self.v)
      
      brick.motor("M4").setPower(self.v)
      
      
      while self.t < 2000:
        self.theta_l = brick.encoder("E4").read()
        self.theta_r = brick.encoder("E3").read()
        self.t = (time.time() * 1000 - self.__interpretation_started_timestamp__) - self.t0
        self.buff = self.buff + "1 " + str(self.v) + " " + str(self.theta_l) + " " + str(self.theta_r) + " " + str(self.t) + " " + str(self.batt) + "\n"
        script.wait(5)
        
      brick.motor("M3").powerOff()
      brick.motor("M4").powerOff()
      
      
      while self.t < 4000:
        self.theta_l = brick.encoder("E4").read()
        self.theta_r = brick.encoder("E3").read()
        self.t = (time.time() * 1000 - self.__interpretation_started_timestamp__) - self.t0
        self.buff = self.buff + "0 " + str(self.v) + " " + str(self.theta_l) + " " + str(self.theta_r) + " " + str(self.t) + " " + str(self.batt) + "\n"
        script.wait(5)
      
      self.batt = brick.battery().readVoltage()
      script.writeToFile("trik_steps.txt", self.buff)
      
      self.v = self.v + 10
    brick.stop()
    return

def main():
  program = Program()
  program.execMain()

if __name__ == '__main__':
  main()
