#RFCOMM sdp Bluetooth Server
from datetime import datetime
import threading
from bluetooth import *
import time

#----------------------------

def blue1():
	try:
		#-----set date ----
		now = datetime.now()
		dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
		date_string = "Xin chào! Bạn đã đăng ký thành công vào lúc: " + dt_string
		#-----------------
		global tam1
#		tam1 = '-'
		server_sock=BluetoothSocket(RFCOMM)
		port = 1
		server_sock.bind(("",port))
		#server_sock.bind(("",PORT_ANY))
		server_sock.listen(1)

		#port =  server_sock.getsockname()[1]

		uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

		advertise_service( server_sock, "Rpi4", service_id = uuid)

		print("Da khoi tao channel: %d"%port)
		client_sock, client_info = server_sock.accept()
		print("Da ket noi thanh cong toi client ", client_info)
		tam1 = client_info[0]
		#f = open("../var/www/html/logfileMAC.log","a+")
		#f.write()

		try:
			while True:
				data = client_sock.recv(1024)
				if len(data) == 0: break
				print("Client gui~: %s" % data)
				datadecode = data.decode('ASCII')
				#print("Type ch 1: ",type(datax)) 
				client_sock.send(date_string)
				f = open("/var/www/html/logfileMAC.log","a")
				f.write(datadecode + " -- " + tam1 + " -- " + dt_string + "\n")
#				f.write(data + "\n")
		except IOError:
			pass

		print("Ket thuc ket noi...")
		client_sock.close()
		server_sock.close()
		print("Done.")

	except:
		print("\n")
#blue1()
#------------------------------2--------------------
def blue2():
	try:
		#-----set date ----
		now = datetime.now()
		dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
		date_string = "Xin chào! Bạn đã đăng ký thành công vào lúc: " + dt_string
                #-----------------
		global tam2
#		tam2 = '!-'
		server_sock=BluetoothSocket(RFCOMM)
		port = 2
		server_sock.bind(("",port))
#		server_sock.bind(("",PORT_ANY))
		server_sock.listen(1)

#		port =  server_sock.getsockname()[1]

		uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

		advertise_service( server_sock, "Rpi4", service_id = uuid)

		print("[2]Da khoi tao channel: %d"%port)
		client_sock, client_info = server_sock.accept()
		print("[2]Da ket noi thanh cong toi client ", client_info )
		tam2 = client_info[0]

		try:
			while True:
				data = client_sock.recv(1024)
				if len(data) == 0: break
				print("[2]Client gui~: %s" % data) 
				datadecode = data.decode('ASCII')
                                #print("Type ch 1: ",type(datax))
				client_sock.send(date_string)
				f = open("/var/www/html/logfileMAC.log","a")
				f.write(datadecode + " -- " + tam2 + "--" + dt_string + "\n")
		except IOError:
			pass

		print("[2]Ket thuc ket noi...")
		client_sock.close()
		server_sock.close()
		print("[2]Done.")
	except:
		print("\n")
#blue2()

#------------------Blue3-----------------------

def blue3():
	try:
		#-----set date ----
		now = datetime.now()
		dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
		date_string = "Xin chào! Bạn đã đăng ký thành công vào lúc: " + dt_string
                #-----------------
		global tam3
#		global client_info
#		tam3 = '-'
		server_sock=BluetoothSocket(RFCOMM)
		port = 4
		server_sock.bind(("",port))
#		server_sock.bind(("",PORT_ANY))
		server_sock.listen(1)

#		port =  server_sock.getsockname()[1]

		uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
				
		advertise_service( server_sock, "Rpi4", service_id = uuid)

		print("Da khoi tao channel: %d"%port)
		client_sock, client_info = server_sock.accept()
		print("Da ket noi thanh cong toi client ", client_info )
		tam3 = client_info[0]

		try:
			while True:
				data = client_sock.recv(1024)
				if len(data) == 0: break
				print("Client gui~: %s" % data)
				datadecode = data.decode('ASCII')
                                #print("Type ch 1: ",type(datax))
				client_sock.send(date_string)
				f = open("/var/www/html/logfileMAC.log","a")
				f.write(datadecode + " -- " + tam3 + "--" + dt_string + "\n")
		except IOError:
			pass

		print("Ket thuc ket noi...")
		client_sock.close()
		server_sock.close()
		print("Done.")
				
	except:
		print("\n")
#blue3()

#---------------------Blue30-----------------------
def blue30():
	try:
		server_sock=BluetoothSocket(RFCOMM)
		port = 30
		server_sock.bind(("",port))
#		server_sock.bind(("",PORT_ANY))
		server_sock.listen(1)

#		port =  server_sock.getsockname()[1]

		uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
				
		advertise_service( server_sock, "Rpi4", service_id = uuid,)

		print("Da khoi tao channel: %d"%port)
		client_sock, client_info = server_sock.accept()
		print("Da ket noi thanh cong toi client ", client_info )
		print("tam1 {}| tam2 {}| tam3 {}| ".format(tam1,tam2,tam3))
		sum_tam = tam1 + '@' + tam2 + '@' + tam3
		print("sum_tam: ",sum_tam)
		try:
#			while True:
				data = client_sock.recv(1024)
#				if len(data) == 0: break
				print("Client gui~: %s" % data)
#				client_sock.send("Xin chao`! Minh la Server Bluetooth")
				client_sock.send(sum_tam)
		except IOError:
			pass

		print("Ket thuc ket noi...")
		client_sock.close()
		server_sock.close()
		print("Client Channel 30 Done.")				
	except:
		print("\n")
#--------------------------------------------------

try:
	b1 = threading.Thread(target = blue1)
	b2 = threading.Thread(target = blue2)
	b3 = threading.Thread(target = blue3)

except Exception as e:
#	print(e)
	print("--------/\-----------")


#-------------------------------------
while True:
	if not (b1.isAlive() or b2.isAlive() or b3.isAlive()):

		b1new = threading.Thread(target = blue1)
		b2new = threading.Thread(target = blue2)
		b3new = threading.Thread(target = blue3)

		b1new.start()
		b2new.start()
		b3new.start()
		print("Da khoi dong xong b1 b2 b3 - delay 1s")
		time.sleep(1)