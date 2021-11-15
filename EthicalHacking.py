import subprocess
import optparse
import re


def get_arguments(): 
  # Allows you to create options which can be passed through in the command line 
  parser = optparse.OptionParser()
  parser.add_option("-i", "--interface", dest="interface", help="Interface to change is its MAC Address")
  parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
  (options, arguments) = parser.parse_args()
  if not options.interface:
    parser.error("[-] Please specify an interface use --help for more info.")
    #code to handle error 
  elif not options.new_mac:
      parser.error("[-] Please specify a new mac, use --help for more info.")
     #code to handle error
  return options 


def change_mac(interface, new_mac):

 print("[+] Changing MAC address for "+ interface + " to " + new_mac) 


#Blocks of Code Seperated By Indentation For Functions 
 subprocess.call(["ifconfig", interface ,"down"])
 subprocess.call(["ifconfig",interface,"hw","ether", new_mac])
 subprocess.call(["ifconfig", interface ,"up"])





# Storing Users Input Variables 
#Returns the arguments and the values 


# Functions set of instructions to carry out a task 
# Can take input, and return result
#inferface = options.interface
#new_mac = options.new_mac
   

options = get_arguments()
change_mac(options.interface, options.new_mac)






