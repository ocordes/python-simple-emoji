"""
pyemoji/emoji.py

wriiten by: Oliver Cordes 2020-05-15
changed by: Oliver Cordes 2020-05-24

"""

#
# References:
#   https://www.webfx.com/tools/emoji-cheat-sheet/
#   http://www.unicode.org/emoji/charts/full-emoji-list.html

"""
Standard modules
"""
import re


# people

#bowtie = ''
smile = '\U0001F604'
simple_smile = '\U0001F642'
laughing = '\U0001F606'
blush = '\U0001F60A'
smiley = '\U0001F603'
relaxed = '\U0001F60C'
smirk = '\U0001F60F'
heart_eyes = '\U0001F60D'
kissing_heart = '\U0001F618'
kissing_closed_eyes = '\U0001F61A'
flushed = '\U0001F633'
relieved = '\U0001F60C'
satisfied = '\U0001F606'
grin = '\U0001F601'
wink = '\U0001F609'
stuck_out_tongue_winking_eye = '\U0001F61C'
stuck_out_tongue_closed_eyes = '\U0001F61D'
grinning = '\U0001F600'
kissing = '\U0001F617'
kissing_smiling_eyes = '\U0001F619'
stuck_out_tongue = '\U0001F61B'
sleeping = '\U0001F634'
worried = '\U0001F61F'
frowning = '\U0001F626'
anguished = '\U0001F627'
open_mouth = '\U0001F62E'
grimacing = '\U0001F62C'
confused = '\U0001F615'
hushed = '\U0001F62F'
neutral = '\U0001F610'
expressionless = '\U0001F611'
unamused = '\U0001F612'
sweat_smile = '\U0001F605'
sweat = '\U0001F613'
disappointed_relieved = '\U0001F625'
weary = '\U0001F629'
pensive = '\U0001F614'
disappointed = '\U0001F61E'
confounded = '\U0001F616'
fearful = '\U0001F628'
cold_sweat = '\U0001F630'
persevere = '\U0001F623'
cry = '\U0001F622'
sob = '\U0001F62D'
joy = '\U0001F602'
astonished = '\U0001F632'  # or '\U0001F635'
scream = '\U0001F631'
neckbeard = ''
tired_face = '\U0001F62B'
yawning_face = '\U0001F971'
angry = '\U0001F620'
rage = '\U0001F621'
triumph = '\U0001F624'
steam_from_nose = triumph
sleepy = '\U0001F62A'
yum = '\U0001F60B'
mask = '\U0001F637'
sunglasses = '\U0001F60E'
dizzy_face = '\U0001F635'
imp = '\U0001F47F'
smiling_imp = '\U0001F608'
neutral_face = neutral
no_mouth = '\U0001F636'
innocent = '\U0001F607'
alien = '\U0001F47D'
yellow_heart = '\U0001F49B'
blue_heart = '\U0001F499'
purple_heart = '\U0001F49C'
heart = '\u2764\uFE0F'
red_heart = heart
green_heart = '\U0001F49A'
orange_heart = '\U0001F9E1'
brown_heart = '\U0001F90E'
black_heart = '\U0001F5A4'
white_heart = '\U0001F90D'
broken_heart = '\U0001F494'
heartbeat = '\U0001F493'
heartpulse = '\U0001F497'
two_hearts = '\U0001F495'
revolving_hearts = '\U0001F49E'
cupid = '\U0001F498'
sparkling_heart = '\U0001F496'
ribbon_heart = '\U0001F49D'
sparkles = '\U00002728'
star = '\U00002B50'
star2 = '\U0001F31F'
dizzy = '\U0001F4AB'
boom = '\U0001F4A5'
collision = boom
anger = '\U0001F4A2'
hundret_points = '\U0001F4AF'
exclamation = '\U00002757'
question = '\U00002753'
grey_exclamation = '\U00002755'
white_exclamation = grey_exclamation
grey_question = '\U00002754'
white_question = grey_question
zzz = '\U0001F4A4'
dash = '\U0001F4A8'
sweat_drops = '\U0001F4A6'
notes = '\U0001F3B6'
musical_note = '\U0001F3B5'
fire = '\U0001F525'
hankey = '\U0001F4A9'
poop = hankey
shit = hankey
thumbsup = '\U0001F44D'
thumbs_up = thumbsup
thumbsdown = '\U0001F44E'
thumbs_down = thumbsdown
ok_hand = '\U0001F44C'
punch = '\U0001F44A'
facepunch = '\U0001F44A'
fist = '\U0000270A'
fist_left = '\U0001F91B'
fist_right = '\U0001F91C'
v = '\U0000270C'
victory = v
wave = '\U0001F44B'
hand = '\U0000270B'
raised_hand = hand
open_hands = '\U0001F450'
vulcan_salute = '\U0001F596'
point_up = '\U0001F446'
point_down = '\U0001F447'
point_left = '\U0001F448'
point_right = '\U0001F449'
middle = '\U0001F595'
raised_hands = '\U0001F64C'
folded_hands = '\U0001F64F'
pray = folded_hands
point_up_2 = '\U0000261D'
clap = '\U0001F44F'
muscle = '\U0001F4AA'
mechanical_arm = '\U0001F9BE'
leg = '\U0001F9B5'
mechanical_leg = '\U0001F9BF'
foot = '\U0001F9B6'
metal = '\U0001F918'
fu = middle
runner = ''
running = ''
couple = ''
family = ''
two_men_holding_hands = ''
two_women_holding_hands = ''
dancer = ''
dancers = ''
ok_woman = ''
no_good = ''
information_desk_person = ''
raising_hand = ''
bride_with_veil = ''
person_with_pouting_face = ''
person_frowning = ''
bow = ''
couplekiss = ''
couple_with_heart = ''
massage = ''
haircut = ''
nail_care = ''
boy = ''
girl = ''
woman = ''
man = ''
baby = ''
older_woman = ''
older_man = ''
person_with_blond_hair = ''
man_with_gua_pi_mao = ''
man_with_turban = ''
construction_worker = ''
cop = ''
angel = ''
princess = ''
smiley_cat = ''
smile_cat = ''
heart_eyes_cat = ''
kissing_cat = ''
smirk_cat = ''
scream_cat = ''
crying_cat_face = ''
joy_cat = ''
pouting_cat = ''
japanese_ogre = ''
japanese_goblin = ''
see_no_evil = ''
hear_no_evil = ''
speak_no_evil = ''
guardsman = ''
skull = ''
feet = ''
lips = ''
kiss = ''
droplet = ''
ear = ''
eyes = ''
nose = ''
tongue = ''
love_letter = ''
bust_in_silhouette = ''
busts_in_silhouette = ''
speech_balloon = ''
thought_balloon = ''
feelsgood = ''
finnadie = ''
goberserk = ''
godmode = ''
hurtrealbad = ''
rage1 = ''
rage2 = ''
rage3 = ''
rage4 = ''
suspect = ''
trollface = ''

# objects



# eat and drink
#beer = :beer:

# function part
"""
now it cames to some functions in the emoji library, which are simple
and using some python tricks!
"""

# emojis converted into a dictionary
__emojis = [attr for attr in dir() if (not attr.startswith('__')) and (not callable(globals()[attr]))]
__emojis_dict = {':'+i+':' : globals()[i] for i in __emojis if globals()[i] != ''}

# regexp pattern for
emoji_pattern = re.compile(r':[a-zA-Z][a-zA-Z0-9_-]*:')

"""
emojize use a regular expression to replace a :emoji_name: word
with the correct unicode if available; multiple occurrences are
allowed!
"""

def emojize(s):

    def repl(matchobj):
        emoji_name = matchobj.group(0)
        return __emojis_dict.get(emoji_name, ':not known:')

    return emoji_pattern.sub(repl, s)
