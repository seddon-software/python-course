'''  
A typical application of callbacks is in the software pattern Pub/Sub (publish and subscribe).
The pattern has a publisher (in our case a TemperaturMonitor) and a number of Observers.  The   
publisher notifies interested parties when an event occurs using a callback.  Typically all the 
observers register with the publisher with an optional condition (in our case the observer 
wants to be notified when the temperature has reached a threshold).
'''

class TemperatureMonitor:
	def setTemperature(self, currentTemperature):
		self.temperature = currentTemperature
		if currentTemperature > 25.0: self.notifyAll()

	def notifyAll(self):
		for callback in TemperatureMonitor.observerCallbacks:
			callback(self.temperature)

	def Register(self, observerCallback):
		TemperatureMonitor.observerCallbacks.append(observerCallback)

	observerCallbacks = []

class Observer:
	def __init__(self, id):
		self.id = id

	def callback(self, temperature):
		print(f"observer {self.id} has been contacted: {temperature}")

	def doRegister(self, temperatureMonitor):
		temperatureMonitor.Register(self.callback)


def main():
	publisher = TemperatureMonitor()
	observer1 = Observer(1)
	observer2 = Observer(2)
	observer3 = Observer(3)
	observer1.doRegister(publisher)
	observer2.doRegister(publisher)
	observer3.doRegister(publisher)

	temperatures = [ 18.0, 21.0, 24.5, 27.3, 26.2, 23.5 ]
	for temperature in temperatures:
		publisher.setTemperature(temperature)

main()
