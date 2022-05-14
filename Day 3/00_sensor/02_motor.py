import YB_Pcb_Car  #Import Yahboom car library
import time

car = YB_Pcb_Car.YB_Pcb_Car()

car.Car_Run(150, 150)
time.sleep(2)
car.Car_Stop()

car.Car_Back(150, 150)
time.sleep(2)
car.Car_Stop()

car.Car_Left(0, 150)
time.sleep(2)
car.Car_Stop()

car.Car_Right(150, 0)
time.sleep(2)
car.Car_Stop()

car.Car_Spin_Left(150, 150)
time.sleep(2)
car.Car_Stop()

car.Car_Spin_Right(150, 150)
time.sleep(2)
car.Car_Stop()

car.Car_Stop()