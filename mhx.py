
import time
import matplotlib
import random


time_slots = 500000
total_delay = 0
total_packets_sent = 0
total_packets_lost = 0
total_packets_created = 0
class Packet:# Define a Packet class to represent network packets
    def __init__(self,packet_id,arrival_time,name):
        self.packet_id = packet_id
        self.arrival_time = arrival_time
        self.name = name
class Station:# Define a Station class to represent network stations
    def __init__(self,station_id,name,wavelength):
        self.station_id = station_id
        self.name = name
        self.wavelength = wavelength
        self.queue = []
    def empty(self):
        return len(self.queue)==0
    def full(self):
        return len(self.queue)==5

propability = float(input("Give me propability :\n"))# Get user input for the probability of packet generation
stations = []# Create a list to hold instances of Station class
wavelength = 1
for i in range(8):# Initialize 8 stations
    station = Station(i,"station"+str(i),wavelength)
    if i==1 or i==3 or i==5:
        wavelength+=1
    stations.append(station)
    
col=0
for j in range(time_slots):# Simulate the network for 500,000 time slots
    wavelengths = []
    for station in stations:#Iterate through each station
        temp1 = random.uniform(0,1)# Generate a random number to determine if a packet is created
        if temp1 <= propability:
            packet = Packet(j,0.001*j,"packet"+str(j))
            total_packets_created+=1
            if not station.full():# Check if the station's queue is not full, add the packet to the queue
                station.queue.append(packet)
            else:
                total_packets_lost+=1
        
        temp2 = random.uniform(0,1)# Generate a random number to determine if a packet is sent
        if temp2 <= 0.5:
            if not station.empty():# Check if the station's queue is not empty
                wavelengths.append(station.wavelength)
                if (wavelengths.count(station.wavelength)<=1):# Check if the wavelength is not already in use (collision)
                    total_packets_sent+=1
                    packet = station.queue.pop()
                    total_delay+=j*0.001 - packet.arrival_time
                else:
                    col+=1
                
               
                
                 
            
   
# Calculate and print simulation results        
average_delay=total_delay/total_packets_sent
throughput=total_packets_sent/time_slots
packet_loss_rate=total_packets_lost/total_packets_created
'''print("Total Delay :",total_delay)
print("Total Packets Created : ",total_packets_created)
print("Total Packets Sent : ",total_packets_sent)
print("Total packets Lost :",total_packets_lost)
print("Total Collisions : ",col)'''
print("Average Delay : ",round(average_delay,4))
print("Throughput : ",round(throughput,4))
print("Packet Loss Rate : ",round(packet_loss_rate,4))

        
    

