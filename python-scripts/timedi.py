"""
Created on Wed Oct 31 19:12:21 2018
@author: jtotten
"""

import re

def main():
	running = True

	while running:
        print('Enter a speed in m/s or as a fraction of the speed of light.')
		print('m/s in the format: x m/s, fraction in the format 0.x')

		speed = input()

        # check input format
		fraction = r'0\.[0-9]+'
		raw_speed = r'[0-9]+[ ]*m/s'
		is_fraction = re.search(fraction, speed)
		is_raw_speed = re.search(raw_speed, speed)

		# if the input is in a correct format
		if is_fraction or is_raw_speed:
            
            if is_raw_speed:
                # remove m/s part of the string and any spaces
				speed = float(speed.split('m/s')[0].strip(' '))
				input_format = 'r'
			elif is_fraction:
				# convert fraction as a string to float
				speed = float(speed)
				input_format = 'f'
			
            # use calc_time_dilation to calculate the amount of time dilation
			# between an obe
			dilation = calc_time_dilation(speed, speed_format=input_format)
			
			print('\nTime dilation relative to stationary observer: {0}\n'.format(dilation))
			print('Press q to quit or any other key to enter another value')
			
			again = input()
			
			if again.lower() == 'q':
                running = False
		else:
			print('Invalid format')

def calc_time_dilation(speed, speed_format='r'):
	# speed of light 
	c = 299792458 
	
	# if the format is a fraction, the speed of light is multiplied
	# by the fraction to get the speed in m/s
	if speed_format == 'f':
		speed = c * speed
	elif speed_format == 'r':
		if speed > c:
			raise ValueError("Speed is greater than that of light")
	else:
		raise ValueError("Speed format must be a string r or f -- raw speed or fraction")
	
	ratio_to_c = (speed ** 2) / (c ** 2)
	dilation = 1 / ((1 - ratio_to_c) ** 0.5)
	return dilation


if __name__ == '__main__':
	main()
