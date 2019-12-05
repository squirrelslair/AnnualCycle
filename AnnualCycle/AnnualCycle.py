#import pgzrun
#pgzrun.go()

WIDTH = 800
HEIGHT = 600
ctr = (WIDTH/2, HEIGHT/2)

# set rotation angles
Jan = 0
Feb = Jan-30
Mar = Feb-30
Apr = Mar-30
May = Apr-30
Jun = May-30
Jul = Jun-30
Aug = Jul-30
Sep = Aug-30
Oct = Sep-30
Nov = Oct-30
Dec = Nov-30

def draw():
    screen.fill((0,0,0))

    month_ring = Actor('month_ring.png', center=ctr)
    month_ring.draw()
    RR_cultivating_and_husbandry()
    TT_fur_trading()
    
def segment(ring, month):
    seg = Actor(ring, center=ctr)
    seg.angle = month
    seg.draw()
    
def RR_planting():
    segment('out1_red_red_river', May)
    
def RR_cultivating_and_husbandry():
    segment('out1_red_red_river', Jun)
    segment('out1_red_red_river', Jul)
    segment('out1_red_red_river', Aug)
    
def RR_harvesting_and_haying():
    segment('out1_red_red_river', Aug)
    segment('out1_red_red_river', Sep)
    segment('out1_red_red_river', Oct)
    
def TT_fur_trading():
    segment('out2_orange_trade_transport', Oct)
    segment('out2_orange_trade_transport', Nov)
    segment('out2_orange_trade_transport', Dec)
    segment('out2_orange_trade_transport', Jan)
    segment('out2_orange_trade_transport', Feb)
    segment('out2_orange_trade_transport', Mar)
    
    #out2_orange_trade_transport = Actor('out2_orange_trade_transport')
    #out3_blue_parkland = Actor('out3_blue_parkland')
    #out4_green_forest = Actor('out4_green_forest')
    #out5_yellow_plains = Actor('out5_yellow_plains')

    
    
    