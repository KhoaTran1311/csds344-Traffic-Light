import pygame
import time

# colors
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# time
GREEN_TIME = 1.5
YELLOW_TIME = 0.5
RED_TIME = 2

# state
VEHICLE_SECURE_STATES = ["NS_GREEN", "EW_GREEN"]

# init Pygame
pygame.init()

# set up pygame
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traffic Light Simulation")

# images
background_image = pygame.image.load("./images/img.png").convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
ped_red_light = pygame.image.load("./images/ped_red.png")
ped_red_light = pygame.transform.scale(ped_red_light, (20,20))
ped_green_light = pygame.image.load("./images/ped_green.png")
ped_green_light = pygame.transform.scale(ped_green_light, (20,20))

# main simulation
def run_simulation():
    x_vehicle_state = "NS_GREEN"
    y_vehicle_state = "NS_RED"

    while True:
        screen.blit(background_image, (0,0))

        if x_vehicle_state == "NS_GREEN":
            draw_traffic_lights(GREEN, RED)
            pygame.display.flip()
            draw_traffic_lights(RED, GREEN)
            pygame.display.flip()
            time.sleep(GREEN_TIME)
            x_vehicle_state = "NS_YELLOW"
        elif x_vehicle_state == "NS_YELLOW":
            draw_traffic_lights(RED, YELLOW)
            pygame.display.flip()
            time.sleep(YELLOW_TIME)
            x_vehicle_state = "NS_RED"
        elif x_vehicle_state == "NS_RED":
            if y_vehicle_state == "NS_RED":
                draw_traffic_lights(RED, RED)
                pygame.display.flip()
                draw_traffic_lights(GREEN, RED)
                pygame.display.flip()
                time.sleep(GREEN_TIME)
                y_vehicle_state = "NS_YELLOW"
            elif y_vehicle_state == "NS_YELLOW":
                draw_traffic_lights(YELLOW, RED)
                pygame.display.flip()
                time.sleep(YELLOW_TIME)
                y_vehicle_state = "NS_RED"
                x_vehicle_state = "NS_GREEN"

        pygame.display.flip()

def draw_traffic_lights(ns_color, ew_color):
    one_set_of_light_horizontal(ew_color, WIDTH // 5, HEIGHT // 4 * 3)
    one_set_of_light_horizontal(ew_color, WIDTH // 5 * 4, HEIGHT // 4)
    one_set_of_light(ns_color, WIDTH // 4, HEIGHT // 5)
    one_set_of_light(ns_color, WIDTH // 4 * 3, HEIGHT // 5 * 4)


def one_set_of_light(color, x, y):
    x_ped = abs(200 - x) + 90
    y_ped = abs(100 - y) // 0.8 + 40
    pygame.draw.rect(screen, "gray17",
                      (x - 15, y-35, 30, 70))
    if color == (0, 255, 0):
        pygame.draw.circle(screen, color,
                       (x, y + 20), 10)
        pygame.draw.circle(screen, (128, 128, 128),
                           (x, y), 10)
        pygame.draw.circle(screen, (128, 128, 128),
                           (x, y - 20), 10)
        pygame.draw.rect(screen, "gray17",
                         (x_ped - 5, y_ped - 5, 30, 30))
        screen.blit(ped_red_light, (x_ped, y_ped))
    elif color == (255, 255, 0):
        pygame.draw.circle(screen, (128, 128, 128),
                       (x, y + 20), 10)
        pygame.draw.circle(screen, color,
                           (x, y), 10)
        pygame.draw.circle(screen, (128, 128, 128),
                           (x, y - 20), 10)
        pygame.draw.rect(screen, "gray17",
                         (x_ped - 5, y_ped - 5, 30, 30))
        screen.blit(ped_red_light, (x_ped, y_ped))
    elif color == (255, 0, 0):
        pygame.draw.circle(screen, (128, 128, 128),
                           (x, y + 20), 10)
        pygame.draw.circle(screen, (128, 128, 128),
                           (x, y), 10)
        pygame.draw.circle(screen, color,
                           (x, y - 20), 10)
        pygame.draw.rect(screen, "gray17",
                         (x_ped-5, y_ped-5, 30, 30))
        screen.blit(ped_green_light, (x_ped, y_ped))

def one_set_of_light_horizontal(color, x, y):
    x_ped = abs(100 - y) // 0.75 + 60
    y_ped = abs(200 - x) + 70
    pygame.draw.rect(screen, "gray17",
                      (x-35, y-15, 70, 30))
    if color == (0, 255, 0):
        pygame.draw.circle(screen, color,
                       (x + 20, y), 10)
        pygame.draw.circle(screen, (128, 128, 128),
                           (x, y), 10)
        pygame.draw.circle(screen, (128, 128, 128),
                           (x - 20, y), 10)
        pygame.draw.rect(screen, "gray17",
                         (x_ped - 5, y_ped - 5, 30, 30))
        screen.blit(ped_red_light, (x_ped, y_ped))
    elif color == (255, 255, 0):
        pygame.draw.circle(screen, (128, 128, 128),
                       (x + 20, y), 10)
        pygame.draw.circle(screen, color,
                           (x, y), 10)
        pygame.draw.circle(screen, (128, 128, 128),
                           (x - 20, y), 10)
        pygame.draw.rect(screen, "gray17",
                         (x_ped - 5, y_ped - 5, 30, 30))
        screen.blit(ped_red_light, (x_ped, y_ped))
    elif color == (255, 0, 0):
        pygame.draw.circle(screen, (128, 128, 128),
                           (x + 20, y), 10)
        pygame.draw.circle(screen, (128, 128, 128),
                           (x, y), 10)
        pygame.draw.circle(screen, color,
                           (x - 20, y), 10)
        pygame.draw.rect(screen, "gray17",
                         (x_ped - 5, y_ped - 5, 30, 30))
        screen.blit(ped_green_light, (x_ped, y_ped))


if __name__ == "__main__":
    run_simulation()
