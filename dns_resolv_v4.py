#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re            #regular expressions.
import subprocess    #to call Subprocess, like nslookup.
import asyncio       #async methods

async def call_nslookup(dns_name):

   ExReg_ip = "Address: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
   process = subprocess.Popen(["nslookup", dns_name], stdout=subprocess.PIPE)
   output_tuple = process.communicate()[0].decode('utf-8')
   match = re.search(ExReg_ip, output_tuple)
   if match:
      print(f'You are asking about this ip address: {match.group(1)} for {dns_name}')
   else:
      print(f'We have not find any ip address for {dns_name}')
   await asyncio.sleep(0.1)

async def main():
   # read from dns names file and to add this names in array.
   f_name = open("./dns_list.txt", "r")
   list_names = f_name.read().split('\n')
   for element in list_names:
      await asyncio.gather(call_nslookup(element))
   f_name.close()
   f_result = open("./result.txt", "a")
   f_result.write ("VOLUMEN TEST - ")
   f_result.close()
   #print ("Please, please press any key to finished program... ")
   #domain2 = input ()
if __name__ == "__main__":
    asyncio.run(main())
