# Import the time and ADS1x15 module.
import time, Adafruit_ADS1x15, os

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

#Gain of 1 = +/-4.096V
GAIN = 8
MAXC = 27781		# max counts at peak accuracy val
MAXV = 3.5		# Max accurate Volts as measured by my Fluke

iterations = 15
avg0 = 0.0
avg1 = 0.0
peakV0 = 0.0
peakV1 = 0.0
percent0 = 0.0
percent1 = 0.0
sampleRate = 0.5	# in seconds
sum = 0.0
avg = 0.0
avg15s = 0.0
loop = 0
n = 0
peakAvg = 0
winner = ""
loser = ""
volts0 = 0.0
volts1 = 0.0
loserV = 0.0

def cls():									#clears the screen
	os.system('cls' if os.name=='nt' else 'clear')

cls()	# clears the screen

for loop in range(0, iterations):
#	if loop >= 1:								# this is so we only calculate the average after the first loop
#		avg = float("{0:.2f}".format(sum/loop ))			# average for the whole run
#		avg0 = float("{0:.2f}".format(avg0*(n-1)/n + volts0/n))		# its more of a 7.5s average lol
#		avg1 = float("{0:.2f}".format(avg1*(n-1)/n + volts1/n))		# its more of a 7.5s average lol
	counts0 = adc.read_adc(0, gain=GAIN)					# integer value from ADC
	counts1 = adc.read_adc(1, gain=GAIN)					# integer value from ADC
	percent0 = float(counts0)/MAXC						# convert to fraction
	percent1 = float(counts1)/MAXC						# convert to fraction
	volts0 = abs(float("{0:.2f}".format((percent0*MAXV))))				# convert to volts
	volts1 = abs(float("{0:.2f}".format((percent1*MAXV))))				# convert to volts
#	if volts0 <0:
#		volts0*-1
#	if volts1 <0:
#		volts1*-1
	if peakV0 <= volts0:							# determine the highest volt measurement
		peakV0 = volts0
	if peakV1 <= volts1:							# determine the highest volt measurement
		peakV1 = volts1
	print' |  Yellow Volts:', format(volts0, ".2f"),' |  White Volts:', format(volts1, ".2f"),' |  Time remaining: ', iterations - loop - 1
	if n <3:								# for the rolling x sec average
		n=n+1
#	sum = sum + volts                                                       # for the rolling x sec average
	time.sleep(0.5)								# wait a half a second before next iteration
#	cls()	# clears the screen

if peakV0 > peakV1:
	winner = "Yellow"
	winnerV = peakV0
	loser = "White"
	loserV = peakV1
else:
	winner = "White"
	winnerV = peakV1
	loser = "Yellow"
	loserV = peakV0

# summary report:
print
print
print('-' * 80)
print
print"  |  GREAT JOB!!!  "
print"  |  The winner is: ", winner, "!!!!  Your Best Voltage Reading was: ", format(winnerV, ".2f"),"V  |  "
print"  |  Too Bad, So Sad! :(           ", loser,  "only read", format(loserV, ".2f"),"V.             |  "
print
print

