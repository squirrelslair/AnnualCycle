import pygame, os, time

WIDTH, HEIGHT = 800, 600 # 1778, 1000  # dimensions of our game window
# 4k is 3840 x 2160, 1.77 ratio

# FPS = 30 # frames per second
FRAME = int(HEIGHT * 0.05)
TOP_PANEL_WIDTH = WIDTH - 2 * FRAME
TOP_PANEL_HEIGHT = int(HEIGHT/2) - 2 * FRAME
TOP_PANEL_SIZE = (TOP_PANEL_WIDTH, TOP_PANEL_HEIGHT)

BOTTOM_PANEL_WIDTH = WIDTH - 2 * FRAME
BOTTOM_PANEL_HEIGHT = int(HEIGHT/2) - 2 * FRAME
BOTTOM_PANEL_SIZE = (BOTTOM_PANEL_WIDTH, BOTTOM_PANEL_HEIGHT)

TOP_PANEL_LOCATION = (FRAME, FRAME)
BOTTOM_PANEL_LOCATION = (FRAME, TOP_PANEL_HEIGHT + 3 * FRAME)

RESET_THRESHOLD = 30 #needs to be 30, set really high for debug

# image parameters
img_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
backgrColour = [125, 125, 125]

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
calendar_table_img = loadImg('calendar_table_white_back.png', BOTTOM_PANEL_SIZE)
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
    screen.fill(backgrColour)
    screen.blit(buttons_img, TOP_PANEL_LOCATION)
    screen.blit(calendar_table_img, BOTTOM_PANEL_LOCATION)

def draw_active_overlays(ols):
    for img in ols:
        screen.blit(img, BOTTOM_PANEL_LOCATION)
        pygame.display.flip()

def is_conflict (act1, act2):
    if (act1 == overlay_plant_img and act2 == overlay_freight_img ):
        return "You can't plant a crop and be away freighting at the same time. "
    
    if (act1 == overlay_plant_img and act2 == overlay_goose_spring_img ):
        return "You can't plant a crop and go goose hunting at the same time. "
    
    if (act1 == overlay_cultivate_img and act2 == overlay_freight_img ):
        return "You can't cultivate and take care of your crop and be away freighting at the same time. "
    
    if (act1 == overlay_cultivate_img and act2 == overlay_buffalo_spring_img ):
        return "You can't take care of your crop and be away buffalo hunting at the same time. "
    
    if (act1 == overlay_harvest_img and act2 == overlay_freight_img ):
        return "You can't harvest your crop and be away freighting at the same time. "
    
    if (act1 == overlay_harvest_img and act2 == overlay_buffalo_fall_img ):
        return "You can't harvest your crop and be away freighting at the same time. "
    
    if (act1 == overlay_harvest_img and act2 == overlay_goose_fall_img ):
        return "You can't harvest your crop and be away goose hunting at the same time. "
    
    if (act1 == overlay_industry_img and act2 == overlay_trade_img ):
        return "You can't harvest your crop and be away goose hunting at the same time. "
    
    if (act1 == overlay_industry_img and act2 == overlay_trap_img ):
        return "You can't do domestic industry and be away trapping at the same time. "
    
    if (act1 == overlay_industry_img and act2 == overlay_buffalo_fall_img ):
        return "You can't do domestic industry and be away buffalo hunting at the same time. "
    
    if (act1 == overlay_industry_img and act2 == overlay_fish_img ):
        return "You can't do domestic industry and be away fishing at the same time. "
    
    if (act1 == overlay_industry_img and act2 == overlay_sugar_img ):
        return "You can't do domestic industry and be away sugaring at the same time. "
    
    if (act1 == overlay_freight_img and act2 == overlay_goose_spring_img ):
        return "You can't go freighting and goose hunting at the same time. "
    
    if (act1 == overlay_freight_img and act2 == overlay_buffalo_spring_img ):
        return "You can't go freighting and be away buffalo hunting at the same time. "
    
    if (act1 == overlay_freight_img and act2 == overlay_goose_fall_img ):
        return "You can't go freighting and be away goose hunting at the same time. "
    
    if (act1 == overlay_trade_img and act2 == overlay_trap_img ):
        return "You can't go trading and trapping at the same time. "
    
    if (act1 == overlay_trade_img and act2 == overlay_buffalo_fall_img ):
        return "You can't go trading and buffalo hunting at the same time. "
    
    if (act1 == overlay_trade_img and act2 == overlay_fish_img ):
        return "You can't go trading and fishing at the same time. "
    
    if (act1 == overlay_trade_img and act2 == overlay_sugar_img ):
        return "You can't go trading and be sugaring at the same time. "
    
    if (act1 == overlay_buffalo_fall_img and act2 == overlay_goose_fall_img ):
        return "You can't go buffalo hunting and goose hunting at the same time. "
    
    if (act1 == overlay_buffalo_fall_img and act2 == overlay_fish_img ):
        return "You can't go buffalo hunting and fishing at the same time. "
    else:
        return ""

def write_and_fade_error(err):
    print(err)
    # write error (explain which can't be done together) on top of the display of the button panel
    # fade the conflicting items and the error back to gray over 3s


def resolve_conflicts(ols, activity):
    
    if activity in ols:
        ols.remove(activity)
        
    else:  
        if ols: # ie if the set is not empty
            for i in ols.copy(): # for each activity in overlays
                c = is_conflict (i, activity)
                if c > "":
                    write_and_fade_error(c)
                    break # break out of for loop
                else:
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

                # if there was ANY button, reset timer
                cycle_start = time.time()
                # if there was a change, redraw
                draw_base_screen()
                draw_active_overlays(overlays)
                pygame.display.flip()




pygame.quit()
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             