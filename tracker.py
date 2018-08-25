'''
@author:
Carlos Jose Fragoso Santoni.
Simple python script for tracking single ip address or using output from netstat -nl -p tcp outcome.


'''
import sys
import requests
from colors import colors
import subprocess as sp


def get_location(ip):
	r = requests.get('http://ip-api.com/json/{ip}'.format(ip=ip))
	j = r.json()
	try:
		query = j['query']
		org = j['org']
		country = j['country']
		isp = j['isp']
		timezone = j['timezone']
		city = j['city']
		lat = j['lat']
		lon = j['lon']
		print(colors.HEADER+" Ip: {ip}\n Organization: {org}\n ISP: {isp}\n Timezone: {timezone}\n Country: {country}\n City: {city}\n lat: {lat}\n lon: {lon}".format(ip=query,org=org,isp=isp,timezone=timezone,country=country,city=city,lat=lat,lon=lon))
	
	except:
		print(j)

def get_location_all_conns():
	net = sp.check_output(['netstat','-nl','-p','tcp'])
	net = net.decode('utf-8')
	net = net.split('\n')
	d = []
	ips = []
	fips = []
	for f in net:
		k = f.split(' ')
		d.append(k)
	for u in d:
		for l in u:
			try:
				y = int(l[0])
				ips.append(l)
			except:
				pass
	for i in ips:
		if i !='0':
			fips.append(i)
		else:
			pass
	for f in fips:
		if f[:3] == '10.':
			fips.remove(f)
	l = list(range(0,len(fips)))
	for t in l:
		if fips[t][-2:][0] == '.':
			fips[t] = fips[t][:-2]
		elif fips[t][-4:][0] == '.':
			fips[t] = fips[t][:-4]
		else:
			fips[t] = fips[t][:-5]
	for ip in fips:
		get_location(ip)
		print('\n')	

if __name__ == "__main__":
#run tracker on specific ip or netstat -nl -p tcp outcome
	try:
		if sys.argv[1] == '-a':
			get_location_all_conns()
		else:
			get_location(sys.argv[1])
	except:
		print("Usage -a for all conns\n tracker <ip> for specific ip")

