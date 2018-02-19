
import pandas as pd
import numpy as np
from surprise import Reader,SVD
import os
import time
import vlc
import sys
from os.path import expanduser


def set_artists(x,artists):
	a = x.replace('-',' ').strip().split(' ')
	a = list(map(str.lower,a))
	for k in artists:
		if k in a:
			return artists[k]
	return "Unknown"

def main():
	media_path = "/../../media/dangar/Important/songs/eng collection/lyrics video/" 
	home = expanduser("~")
	try:
		local_songs_df = pd.read_csv('local_songs_data.csv')
	except:
		local_songs_df = pd.DataFrame()
		local_songs_df['song_name'] = os.listdir(media_path)
		local_songs_df['listen_counter'] = 0
		local_songs_df['ratings'] = 0



	artists = {'linkin':'Linkin Park','coldplay':'Coldplay','akon':'Akon','garrix':'Martin Garrix',
			   'avicii':'Avicii','script':'The Script','minaj':'Nicki Minaj','bruno':'Bruno Mars',
			   'bebe':'Bebe Rexha','calvin':'Calvin Harris','camila':'Camila Cabello','charlie':'Charlie Puth',
			  'bandit':'Clean Bandit','alan':'Alan Walker','guetta':'David Guetta','sheeran':'Ed Sheeren',
			   'fonsi':'Luis Fonsi','shakira':'Shakira', 'onerepublic':'OneRepublic','taylor':'Taylor Swift',
			   'weeknd':'The Weeknd','snake':'Dj Snake','eminem':'Eminem','iglesias':'Enrique Iglesias','eazy':'G-Eazy',
			   'halsey':'Halsey','dragons':'Imagine Dragons','bieber':'Justin Bieber','katy':'Katy Perry','kygo':'Kygo',
			   'maroon' : 'Maroon 5','nf':'NF','pitbull':'Pitbull','gomez':'Selena Gomez','sia':'Sia','chainsmokers':'The Chainsmokers',
			   'score':'The Score','pilots':'Twenty One Pilots','zayn':'ZAYN'
			  }




	local_songs_df['artists'] =local_songs_df.song_name.apply(lambda x: set_artists(x,artists))
	local_songs_df.listen_counter.fillna(value=0,inplace=True)
	local_songs_df.ratings.fillna(value=0,inplace=True)
	local_songs_df['score'] = local_songs_df.ratings*0.67 + local_songs_df.listen_counter * 0.33

	local_songs_df.sort_values(by='score',ascending=False,inplace=True)

	local_songs_df.reset_index(inplace=True,drop=True)

	os.chdir(media_path)


	# In[14]:


	# def play(x):
	#     player = vlc.MediaPlayer(x)
	#     player.play()
	#     print("Playing : {} ".format(x[:-4]))
	#     x1,x2=0,1
	#     while x1!=x2:
	#         x1 = player.get_time()
	#         time.sleep(2)
	#         x2 = player.get_time()
	#     c = int(input("Rate This Song in 1 to 10 : "))
		
	#     print("{} rank is saved \n Thank you for your support".format(c))
	#     print('----------------------*****----------------------')
	#     player.stop()
		

	#local_songs_df.song_name.apply(play)
	#song_count = int(input("There are {} songs in your library\nHow many songs May I recommend you?".format(len(local_songs_df))))
	j = 0
	for x in local_songs_df.song_name:
		try:
			j+=1
			repeat = 'yes'
			# player = vlc.MediaPlayer(x)
			# player.play()
			# print("{}) song \nPlaying : {} ".format(j,x[:-4]))
			# x1,x2=0,1
			# while x1!=x2:
			# 	x1 = player.get_time()
			# 	time.sleep(2)
			# 	x2 = player.get_time()
			# repeat = input('Want to repeat this song ? (yes/no) :> ')
			while repeat=='yes' or repeat=='Yes':
				player = vlc.MediaPlayer(x)
				player.play()
				print("{}) song \nPlaying : {} ".format(j,x[:-4]))
				x3,x4=0,1
				while x3!=x4:
					x3 = player.get_time()
					time.sleep(2)
					x4 = player.get_time()
				if (local_songs_df.loc[local_songs_df.song_name == x,'ratings']==0).bool():
					c = int(input("Rate This Song in 1 to 10 : "))
					local_songs_df.loc[local_songs_df.song_name == x,'ratings'] = c
					print("{} rank is saved \n Thank you for your support".format(c))
				local_songs_df.loc[local_songs_df.song_name == x,'listen_counter'] += 1
				print('You have listened this song {} times'.format(int(local_songs_df.loc[local_songs_df.song_name == x,'listen_counter'])))
				print('----------------------*****----------------------')
				print()
				player.stop()
				repeat = input('Want to repeat this song ? (yes/no) :> ')
				if repeat=='yes':
					print(' Yeah !! You like this song too much')
		except (KeyboardInterrupt, SystemExit):
			local_songs_df.to_csv(home+'/local_songs_data.csv')
			print('Want to Quit? \n wait let me save the data')
			print('Saving....')
			time.sleep(5)
			player.stop()
			print('Done!!!!')
			sys.exit()


		local_songs_df.to_csv(home+'/local_songs_data.csv')

if __name__=='__main__':
	main()