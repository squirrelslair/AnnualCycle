#import pgzrun
import time
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

# set file names for segment images
RedRiver = "out1_red_red_river"
Trade = "out2_orange_trade_transport"
Parkland = "out3_blue_parkland"
Forest = "out4_green_forest"
Plains = "out5_yellow_plains"

# build data structure to contain cycle data
# a set of months for each geographical region / ring
Cycle = {
    RedRiver : set(),
    Trade : set(),
    Forest : set(),
    Plains : set(),
    Parkland : set(),
}

# define the sets of months for activities
RR_planting = {May}
RR_cultivating_and_husbandry = {Jun, Jul, Aug}
RR_harvesting_and_haying = {Aug, Sep, Oct}
RR_domestic_industry = {Oct, Nov, Dec, Jan, Feb, Mar}
TT_fur_trading = {Oct, Nov, Dec, Jan, Feb, Mar}
TT_trading_pemmican = {Oct, Nov}
TT_long_distance_freighting = {May, Jun, Jul, Aug, Sep, Oct}
TT_trading_produce = {Sep, Oct, Nov}
Forest_trapping_hunting = {Oct, Nov, Dec, Jan, Feb, Mar}
Plains_bison_hunt = {May, Jun, Jul, Aug, Sep, Oct}
Parkland_lake_fishing = {Oct, Nov, Dec, Jan, Feb}
Parkland_sugaring = {Oct, Nov, Dec, Jan, Feb, Mar}
Parkland_goose_hunting = {Sep}
Parkland_trapping_hunting = {Oct, Nov, Dec, Jan, Feb, Mar}

def on_key_down(key):
    if   key.name == "F":
        Cycle[Forest] = Cycle[Forest].union(Forest_trapping_hunting)
    elif key.name == "P":
        Cycle[Plains] = Cycle[Plains].union(Plains_bison_hunt)
    elif key.name == "C":
        Cycle[RedRiver] = Cycle[RedRiver].union(RR_cultivating_and_husbandry)
    elif key.name == "H":
        Cycle[RedRiver] = Cycle[RedRiver].union(RR_harvesting_and_haying)
    elif key.name == "D":
        Cycle[RedRiver] = Cycle[RedRiver].union(RR_domestic_industry)
    else:
        print ("still need other keydowns, and GPIO processors")
    print(key.name)
    
def update():
    # this automatically runs before draw...
    print ("updating now")    

def draw():
    screen.fill((0,0,0))
    
    month_ring = Actor('month_ring.png', center=ctr)
    month_ring.draw()
    
    # draw the ring months currently in data structure
    for each_ring, ring_months in Cycle.items():
        for each_month in ring_months:
            #print (each_ring, each_month)
            segment(each_ring, each_month)

    clock.schedule_unique(print_delay(), 1.0)
            
    # highlight the segments where two rings use the same month
    # yes this will trigger twice for each match but so what?
    for ring1, ring_months1 in Cycle.items():
        for ring2, ring_months2 in Cycle.items():
            for month1 in ring_months1:
                for month2 in ring_months2:
                    if month1 == month2 and ring1 != ring2:
                        print ("both " + ring1 + " and " + ring2 + " have month " + str(month1))
                        segment(ring1 + "_blinky", month1)
                        segment(ring2 + "_blinky", month2)
    #clock.schedule_unique(delay_print(), 1.0)
    
    # after drawing, reset data structure for the ring
    reset_ring()
    
     
def segment(ring, month):
    seg = Actor(ring, center=ctr)
    seg.angle = month
    seg.draw()
    
def reset_ring():
    # clear the cycle's datastructure
    for each_ring, ring_months in Cycle.items():
        ring_months.clear()
        
def print_delay():
    print("delaying")


#for x, y in Cycle.items():
#    print(x, y) 

#for each_ring, ring_months in Cycle.items():
#    for each_month in ring_months:
#        print (each_ring, each_month)



