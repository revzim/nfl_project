#python read
projections = open('projections.txt', 'r+')
first_read_projections = projections.read()
read_projections = first_read_projections.split('Value', 1)[1]
read_projections.strip()

data = []
data.append(read_projections.split('\t'))
data = data[0]
players =[]
for d in data:
    players.append(d.splitlines())
new_players = []
for player in players:
    player = player
    for p in player:
        new_players.append(p)
player_stats =[]
for p in new_players:
    p.replace('\t', ' ')
    player_stats.append(p.replace(',',' ').replace('(', ' ').replace(')', ' ').split())
class Player:
    def __init__(self, player_fname, player_lname, player_pos, player_team, opp_team, opp_rank, ranks_ovr, ranks_pos, passing_yds, passing_tds, passing_ints, rushing_att, rushing_yds, rushing_tds, receiving_rec, receiving_yds, receiving_tds, numberFive_fp, fanduel_fp, fanduel_cost, fanduel_value):
        self.player_fname = player_fname
        self.player_lname = player_lname
        self.player_pos = player_pos
        self.player_team = player_team
        self.opp_team = opp_team
        self.opp_rank = opp_rank
        self.ranks_ovr = ranks_ovr
        self.ranks_pos = ranks_pos
        self.passing_yds = passing_yds
        self.passing_tds = passing_tds
        self.passing_ints = passing_ints
        self.rushing_att = rushing_att
        self.rushing_yds = rushing_yds
        self.rushing_tds = rushing_tds
        self.receiving_rec = receiving_rec
        self.receiving_yds = receiving_yds
        self.receiving_tds = receiving_tds
        self.numberFive_fp = numberFive_fp
        self.fanduel_cost = fanduel_cost
        self.fanduel_value = fanduel_value
player_stats.pop(0)
#print player_stats
player_objs = []
for stat in player_stats:
    fname = stat[0]
    lname = stat[1]
    ppos = stat[2]
    pteam = stat[3]
    o_team = stat[4]
    o_rank = stat[5]
    r_ovr = stat[6]
    r_pos = stat[7]
    p_yds = stat[8]
    p_tds = stat[9]
    p_ints = stat[10]
    r_att = stat[11]
    r_yds = stat[12]
    r_tds = stat[13]
    rec_rec = stat[14]
    rec_yds = stat[15]
    rec_tds = stat[16]
    num_five_fp = stat[17]
    fanduel_cost = stat[18]
    fanduel_value = stat[19]
    playas = Player(fname, lname, ppos, pteam, o_team, o_rank, r_ovr, r_pos, p_yds, p_tds, p_ints, r_att, r_yds, r_tds, rec_rec, rec_yds, rec_tds, num_five_fp, fanduel_cost, fanduel_value, 0)
    player_objs.append(playas)
    #print playas

#print player_objs

for player in player_objs:
    print player.player_fname, player.player_lname
chosen_player = ''
def get_player():
    print 'Which player\'s stats would you like to view?'
    chosen_player = raw_input()
    if chosen_player == "%s %s" % (player.player_fname, player.player_lname):
        print 'Please wait while we search up your stats...'
    else:
        print 'Player not in list, choose new player:'
        chosen_player = raw_input()
    return chosen_player
#get_player()

def get_player_stats():
    player = get_player()
    for p in player_objs:
        fullname = "%s %s" % (p.player_fname, p.player_lname)
        if player == fullname:
            attrs = vars(p)
            print '\n'.join("%s: %s" % item for item in attrs.items())
get_player_stats()
