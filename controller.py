# controller.py

# Controller class does not depend on any specific device
class Controller:

    def operate_device(self, device):
        # Accepts ANY device object
       outputs=[]  #empty list
       outputs.append(device.start())
       outputs.append(device.stop())
       return outputs
