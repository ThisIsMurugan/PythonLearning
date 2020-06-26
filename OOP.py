class Customer:
    CustomerName=""
    CustomerCode=""
    def Add(self):
        print(" Add called ")

custObj = Customer()
custObj.Add()
custObj.CustomerName = "Murugan"
custObj.CustomerCode = "C001"
custObj.Add()
print(custObj.CustomerCode)
print(custObj.CustomerName)