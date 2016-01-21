import thread
import threading
import time

# Define a function for the thread
def print_time(threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )


exitFlag = 0
threadLock = threading.Lock()

class myThread (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print "Starting " + self.name
		threadLock.acquire()
		print_time(self.name, self.counter, 5)
		print "Exiting " + self.name
		threadLock.release()

def print_time(threadName, delay, counter):
	while counter:
		if exitFlag:
			threadName.exit()
		time.sleep(delay)
		print "%s: %s" % (threadName, time.ctime(time.time()))
		counter -= 1


if __name__ == '__main__':
	
	# try:
	# 	thread.start_new_thread( print_time, ("Thread-1", 2) )
	# 	thread.start_new_thread( print_time, ("Thread-2", 4) )
	# except:
	# 	print "Error: unable to start thread"

	# count = 0
	# while count < 5:
	# 	time.sleep(10)
	# 	count += 1

	# Create new threads
	thread1 = myThread(1, "Thread-1", 1)
	thread2 = myThread(2, "Thread-2", 2)

	# Start new Threads
	thread1.start()
	thread2.start()
	thread2.join()
	thread1.join()
	print "Exiting Main Thread"

