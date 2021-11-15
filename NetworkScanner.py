
import scapy.all as scapy
import optparse

def args():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="IP Address to Scan")
    (options, arguments) = parser.parse_args()
    if not options.target:
     parser.error("[-] Please specify an interface use --help for more info.")
    #code to handle error 
    return options 


def scan(ip):
    #Find Out who has specific IP Address and Send to GRouter
    arp_request = scapy.ARP(pdst=ip)
    #arp_request.show()
    #Return Mac Address to Broadcast MAC Address 
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #broadcast.show()
    #scapy allows you to combine variables using forward slash
    arp_request_broadcast= broadcast/arp_request
   

    #By Setting Verbose to False means that I don't see packet info
    #Send packets and wait for answered and unanswered responses
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    
    #print(answered_list.summary())

    #T\ Prints Tab And N---- means next line 
    print("IP\t\t\tMAC Address\n----------------------------------")
    clients_list = []
    for element in answered_list:
        #Dictionary Being Created 
        #client_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc}
        #Adds the values of the dictionary to the cilent list above
        #clients_list.append(client_dict)
        print(element[1].psrc) #+ "\t\t" + element[1].hwsrc)
        print(element[1].hwsrc)
        print("----------------------------------")

        #print(element[2].psrc + "\t\t" + element[2].hwsrc)
        #print(clients_list)

# Prints Results After Creating Dictionary

# def print_result(results_list):
#      print("IP\t\t\tMAC Address\n----------------------------------")
#      for client in results_list:
#        print(client["ip"] + "\t\t" + client["mac"])
       

options = args()
scan_result = scan(options.target)
#print_result=(scan_result)






    #arp_request_broadcast.show()
    #print(arp_request_broadcast.summary())

    #print(broadcast.summary())

    #Returns Details for THis 
    #scapy.ls(scapy.Ether())
    
    #print(arp_request.summary())
    
    #Lists the fields we can set 
    #scapy.ls(scapy.ARP)

    #gives you the fields or variables you want to find out 
    #scapy.ls(scapy.ARP())


    #scapy.arping(ip)

#IP Address to Scan 
#scan("192.168.1.76/24")
