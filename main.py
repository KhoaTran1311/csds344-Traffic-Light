
import pygame
import sys
import time

# Constants for colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Constants for time durations in seconds
GREEN_TIME = 16
YELLOW_TIME = 8
RED_TIME = 10
PED_GREEN_TIME = 8

# Constants for simulation state
VEHICLE_SECURE_STATES = ["NS_GREEN", "EW_GREEN"]
PED_SECURE_STATES = ["WALK"]

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traffic Light Simulation")

# Main simulation loop
def run_simulation():
    x_vehicle_state = "NS_GREEN"
    y_vehicle_state = "NS_RED"
    ped_state = "WALK"

    while True:
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()

        if x_vehicle_state == "NS_GREEN":
            draw_traffic_lights(RED, RED)
            draw_pedestrian_lights(GREEN)
            pygame.display.flip()
            time.sleep(PED_GREEN_TIME)
            draw_pedestrian_lights(RED)
            draw_traffic_lights(RED, GREEN)
            pygame.display.flip()
            time.sleep(GREEN_TIME - PED_GREEN_TIME)
            x_vehicle_state = "NS_YELLOW"
        elif x_vehicle_state == "NS_YELLOW":
            draw_traffic_lights(RED, YELLOW)
            draw_pedestrian_lights(RED)
            pygame.display.flip()
            time.sleep(YELLOW_TIME)
            x_vehicle_state = "NS_RED"
        elif x_vehicle_state == "NS_RED":
            if y_vehicle_state == "NS_RED":
                draw_traffic_lights(RED, RED)
                draw_pedestrian_lights(GREEN)
                pygame.display.flip()
                time.sleep(PED_GREEN_TIME)
                draw_pedestrian_lights(RED)
                draw_traffic_lights(GREEN, RED)
                pygame.display.flip()
                time.sleep(GREEN_TIME - PED_GREEN_TIME)
                y_vehicle_state = "NS_YELLOW"
            elif y_vehicle_state == "NS_YELLOW":
                draw_traffic_lights(YELLOW, RED)
                draw_pedestrian_lights(RED)
                pygame.display.flip()
                time.sleep(YELLOW_TIME)
                y_vehicle_state = "NS_RED"
                x_vehicle_state = "NS_GREEN"

        pygame.display.flip()

def draw_traffic_lights(ns_color, ew_color):
    light_width = 20
    light_height = 40
    pygame.draw.rect(screen, ns_color,
                     (WIDTH // 2 - light_width // 2, HEIGHT // 3 - light_height // 2, light_width, light_height))
    pygame.draw.rect(screen, ns_color,
                     (WIDTH // 2 - light_width // 2, HEIGHT // 3 * 2 - light_height // 2, light_width, light_height))
    pygame.draw.rect(screen, ew_color,
                     (WIDTH // 3 - light_height // 2, HEIGHT // 2 - light_width // 2, light_height, light_width))
    pygame.draw.rect(screen, ew_color,
                     (WIDTH * 2 // 3 - light_height // 2, HEIGHT // 2 - light_width // 2, light_height, light_width))


def draw_pedestrian_lights(color):
    radius = 20
    pygame.draw.circle(screen, color, (WIDTH // 6, HEIGHT // 2), radius)
    pygame.draw.circle(screen, color, (WIDTH * 5 // 6, HEIGHT // 2), radius)
    pygame.draw.circle(screen, color, (WIDTH // 2, HEIGHT // 6), radius)
    pygame.draw.circle(screen, color, (WIDTH // 2, HEIGHT * 5 // 6), radius)

if __name__ == "__main__":
    run_simulation()
