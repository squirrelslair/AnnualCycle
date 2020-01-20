import pygame, os, time

# buttons image is 3751 x 1666
# schedule image is 3751 x 680
# we'd want to display it with a 10%  frame

WIDTH, HEIGHT = 1280, 720 # dim for debugging
# WIDTH, HEIGHT = 2560, 1440 # the monitor they chose
# https://www.amazon.ca/dp/B0787XMLZQ/ref=s9_acsd_simh_bw_c2_x_0_i?pf_rd_m=A1IM4EOPHS76S7&pf_rd_s=merchandised-search-6&pf_rd_r=9ZXXDXVGTQW57HYR0SXF&pf_rd_t=101&pf_rd_p=5233d856-97c0-4cdd-b746-6135fe6f2774&pf_rd_i=677246011

TOP_PANEL_WIDTH = WIDTH 
TOP_PANEL_HEIGHT = int(HEIGHT/2)
TOP_PANEL_SIZE = (TOP_PANEL_WIDTH, TOP_PANEL_HEIGHT)
TOP_PANEL_CENTRE = (TOP_PANEL_WIDTH/2 , TOP_PANEL_HEIGHT/2)

BOTTOM_PANEL_WIDTH = WIDTH
BOTTOM_PANEL_HEIGHT = int(HEIGHT/2)
BOTTOM_PANEL_SIZE = (BOTTOM_PANEL_WIDTH, BOTTOM_PANEL_HEIGHT)

TOP_PANEL_LOCATION = (0,0)
BOTTOM_PANEL_LOCATION = (0, TOP_PANEL_HEIGHT)

RESET_THRESHOLD = 30 #needs to be 30, set really high for debug

# image parameters
img_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
BACK_COLOUR = [125, 125, 125]

# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #, pygame.FULLSCREEN)
pygame.display.set_caption("Métis")
# clock = pygame.time.Clock(FPS)


# load images
def loadImg(imgnm, size):
    img = pygame.image.load(os.path.join(img_folder, imgnm)).convert_alpha()
    imgScaled = pygame.transform.scale(img, size)
    return imgScaled

buttons_img = loadImg('buttons.png', TOP_PANEL_SIZE)
calendar_table_img = loadImg('calendar_table.png', BOTTOM_PANEL_SIZE)
overlay_buffalo_fall_img = loadImg('overlay_buffalo_fall.png', BOTTOM_PANEL_SIZE)
overlay_buffalo_spring_img = loadImg('overlay_buffalo_spring.png', BOTTOM_PANEL_SIZE)
overlay_cultivate_img = loadImg('overlay_cultivate.png', BOTTOM_PANEL_SIZE)
overlay_fish_img = loadImg('overlay_fish.png', BOTTOM_PANEL_SIZE)
overlay_freight_img = loadImg('overlay_freight.png', BOTTOM_PANEL_SIZE)
overlay_goose_fall_img = loadImg('overlay_goose_fall.png', BOTTOM_PANEL_SIZE)
overlay_goose_spring_img = loadImg('overlay_goose_spring.png', BOTTOM_PANEL_SIZE)
overlay_harvest_img = loadImg('overlay_harvest.png', BOTTOM_PANEL_SIZE)
overlay_industry_img = loadImg('overlay_industry.png', BOTTOM_PANEL_SIZE)
overlay_plant_img = loadImg('overlay_plant.png', BOTTOM_PANEL_SIZE)
overlay_sugar_img = loadImg('overlay_sugar.png', BOTTOM_PANEL_SIZE)
overlay_trade_img = loadImg('overlay_trade.png', BOTTOM_PANEL_SIZE)
overlay_trap_img = loadImg('overlay_trap.png', BOTTOM_PANEL_SIZE)

def draw_base_screen(): 
    screen.fill(BACK_COLOUR)
    screen.blit(buttons_img, TOP_PANEL_LOCATION)
    screen.blit(calendar_table_img, BOTTOM_PANEL_LOCATION)

def draw_active_overlays(ols):
    for img in ols:
        screen.blit(img, BOTTOM_PANEL_LOCATION)
        pygame.display.flip()

def is_conflict (act1, act2):
    if (act1 == overlay_plant_img and act2 == overlay_freight_img ) or (act2 == overlay_plant_img and act1 == overlay_freight_img ):
        return "You can't plant a crop and be away freighting at the same time. "
    
    if (act1 == overlay_plant_img and act2 == overlay_goose_spring_img ) or (act2 == overlay_plant_img and act1 == overlay_goose_spring_img ):
        return "You can't plant a crop and go goose hunting at the same time. "
    
    if (act1 == overlay_cultivate_img and act2 == overlay_freight_img ) or (act2 == overlay_cultivate_img and act1 == overlay_freight_img ):
        return "You can't cultivate and take care of your crop and be away freighting at the same time. "
    
    if (act1 == overlay_cultivate_img and act2 == overlay_buffalo_spring_img ) or (act2 == overlay_cultivate_img and act1 == overlay_buffalo_spring_img ):
        return "You can't take care of your crop and be away buffalo hunting at the same time. "
    
    if (act1 == overlay_harvest_img and act2 == overlay_freight_img ) or (act2 == overlay_harvest_img and act1 == overlay_freight_img ):
        return "You can't harvest your crop and be away freighting at the same time. "
    
    if (act1 == overlay_harvest_img and act2 == overlay_buffalo_fall_img ) or (act2 == overlay_harvest_img and act1 == overlay_buffalo_fall_img ):
        return "You can't harvest your crop and be away freighting at the same time. "
    
    if (act1 == overlay_harvest_img and act2 == overlay_goose_fall_img ) or (act2 == overlay_harvest_img and act1 == overlay_goose_fall_img ):
        return "You can't harvest your crop and be away goose hunting at the same time. "
    
    if (act1 == overlay_industry_img and act2 == overlay_trade_img ) or (act2 == overlay_industry_img and act1 == overlay_trade_img ):
        return "You can't harvest your crop and be away goose hunting at the same time. "
    
    if (act1 == overlay_industry_img and act2 == overlay_trap_img ) or (act2 == overlay_industry_img and act1 == overlay_trap_img ):
        return "You can't do domestic industry and be away trapping at the same time. "
    
    if (act1 == overlay_industry_img and act2 == overlay_buffalo_fall_img ) or (act2 == overlay_industry_img and act1 == overlay_buffalo_fall_img ):
        return "You can't do domestic industry and be away buffalo hunting at the same time. "
    
    if (act1 == overlay_industry_img and act2 == overlay_fish_img ) or (act2 == overlay_industry_img and act1 == overlay_fish_img ):
        return "You can't do domestic industry and be away fishing at the same time. "
    
    if (act1 == overlay_industry_img and act2 == overlay_sugar_img ) or (act2 == overlay_industry_img and act1 == overlay_sugar_img ):
        return "You can't do domestic industry and be away sugaring at the same time. "
    
    if (act1 == overlay_freight_img and act2 == overlay_goose_spring_img ) or (act2 == overlay_freight_img and act1 == overlay_goose_spring_img ):
        return "You can't go freighting and goose hunting at the same time. "
    
    if (act1 == overlay_freight_img and act2 == overlay_buffalo_spring_img ) or (act2 == overlay_freight_img and act1 == overlay_buffalo_spring_img ):
        return "You can't go freighting and be away buffalo hunting at the same time. "
    
    if (act1 == overlay_freight_img and act2 == overlay_goose_fall_img ) or (act2 == overlay_freight_img and act1 == overlay_goose_fall_img ):
        return "You can't go freighting and be away goose hunting at the same time. "
    
    if (act1 == overlay_trade_img and act2 == overlay_trap_img ) or (act2 == overlay_trade_img and act1 == overlay_trap_img ):
        return "You can't go trading and trapping at the same time. "
    
    if (act1 == overlay_trade_img and act2 == overlay_buffalo_fall_img ) or (act2 == overlay_trade_img and act1 == overlay_buffalo_fall_img ):
        return "You can't go trading and buffalo hunting at the same time. "
    
    if (act1 == overlay_trade_img and act2 == overlay_fish_img ) or (act2 == overlay_trade_img and act1 == overlay_fish_img ):
        return "You can't go trading and fishing at the same time. "
    
    if (act1 == overlay_trade_img and act2 == overlay_sugar_img ) or (act2 == overlay_trade_img and act1 == overlay_sugar_img ):
        return "You can't go trading and be sugaring at the same time. "
    
    if (act1 == overlay_buffalo_fall_img and act2 == overlay_goose_fall_img ) or (act2 == overlay_buffalo_fall_img and act1 == overlay_goose_fall_img ):
        return "You can't go buffalo hunting and goose hunting at the same time. "
    
    if (act1 == overlay_buffalo_fall_img and act2 == overlay_fish_img ) or (act2 == overlay_buffalo_fall_img and act1 == overlay_fish_img ):
        return "You can't go buffalo hunting and fishing at the same time. "
    else:
        return ""


def display_and_fade_message(bg_colour, msg, fade_time):
    FONT_COLOR = (0,0,0)
    the_error_msg = pygame.font.Font(None, 32) #not setting a font, but could
    the_error = the_error_msg.render(msg, True, FONT_COLOR, bg_colour) #antialiasing set to false so it looks same as other fonts on graphics
    err_rect = the_error.get_rect()
    err_rect.center = pygame.display.get_surface().get_size() 
    err_rect.center = err_rect.center[0] / 2, err_rect.center[1] / 2  #get ctr of window

    print ("must still size automatically") # debug - pygame.display.get_surface().get_size()  * (0.5, 0.5) #get ctr of window

    orig_screen = screen.copy() #get current display
    fade_step = fade_time/255
    
    for i in range (255, -1, -1):   
        screen.fill(bg_colour)
        screen.blit(orig_screen, (0,0))
        the_error.set_alpha(i) #sets transparency
        screen.blit(the_error, err_rect)
        pygame.display.update()
        time.sleep(fade_step)
        

def resolve_conflicts(ols, activity):
    print('resolving conflicts')
    if activity in ols:
        ols.remove(activity)
        print ('activity was already chosen, disabling')
    else:  
        print ('activity was not chosen yet')
        if ols: # ie if the set is not empty
            for i in ols.copy(): # for each activity in overlays
                c = is_conflict (i, activity)
                if c > "":
                    print ('and there was a conflict')
                    display_and_fade_message(BACK_COLOUR, c, 3) #display error c for .. seconds
                    break # break out of for loop
                else:
                    print ('and there was no conflict')
                    ols.add(activity)
        else: #if ols is empty
            ols.add(activity)
                
    return ols


# Main loop:
running = True
while running:
    cycle_start = time.time()
    draw_base_screen()
    overlays = set() # make empty set so python knows this is a set
    draw_active_overlays(overlays)
    pygame.display.flip()

    # until RESET_THRESHOLD time has passed, run this loop
    while cycle_start + RESET_THRESHOLD > time.time():
       
       # Process input (events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # check for closing window
                print("quit has happened")
                running = False
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.unicode == 'b':
                    overlays = resolve_conflicts(overlays, overlay_buffalo_fall_img)
                if event.unicode == 'B':
                    overlays = resolve_conflicts(overlays, overlay_buffalo_spring_img)
                if event.unicode == 'c':
                    overlays = resolve_conflicts(overlays, overlay_cultivate_img)
                if event.unicode == 'f':
                    overlays = resolve_conflicts(overlays, overlay_fish_img)
                if event.unicode == 'm': # m for move
                    overlays = resolve_conflicts(overlays, overlay_freight_img)
                if event.unicode == 'g':
                    overlays = resolve_conflicts(overlays, overlay_goose_fall_img)
                if event.unicode == 'G':
                    overlays = resolve_conflicts(overlays, overlay_goose_spring_img)
                if event.unicode == 'h':
                    overlays = resolve_conflicts(overlays, overlay_harvest_img)
                if event.unicode == 'i':
                    overlays = resolve_conflicts(overlays, overlay_industry_img)
                if event.unicode == 'p':
                    overlays = resolve_conflicts(overlays, overlay_plant_img)
                if event.unicode == 's':
                    overlays = resolve_conflicts(overlays, overlay_sugar_img)
                if event.unicode == 'e': # e for exchange
                    overlays = resolve_conflicts(overlays, overlay_trade_img)
                if event.unicode == 't':
                    overlays = resolve_conflicts(overlays, overlay_trap_img)
                print('----next button---')
                # if there was ANY button, reset timer
                cycle_start = time.time()
                # if there was a change, redraw
                draw_base_screen()
                draw_active_overlays(overlays)
                pygame.display.flip()

pygame.quit()
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             