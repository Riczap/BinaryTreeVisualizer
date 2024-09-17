import pygame
import tkinter as tk
from tkinter import simpledialog
from tkinter import colorchooser

#Global
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 150, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)


class Render:
    def __init__(self, screen):
        self.screen = screen
        self.node_rgb = list(WHITE)
        self.line_rgb = list(WHITE)
        self.background_rgb = list(BLACK)
        self.font = pygame.font.Font(None, 36)
        self.button_font = pygame.font.Font(None, 36)

    def balanced_text_box(self, balanced):
        balanced_surface = self.font.render("Balanced: ", True, WHITE)
        true_surface = self.font.render("True", True, GREEN)
        false_surface = self.font.render("False", True, RED)
        self.screen.blit(balanced_surface, (10, 10))
        if balanced:
            self.screen.blit(true_surface, (10 + balanced_surface.get_width(), 10))
        else:
            self.screen.blit(false_surface, (10 + balanced_surface.get_width(), 10))


    def create_button(self, text, screen_width, offset_y=0):
         
        button_text = self.button_font.render(f"{text}", True, BLACK)


        padding_x = 10
        padding_y = 5


        button_width = button_text.get_width() + 2 * padding_x
        button_height = button_text.get_height() + 2 * padding_y
        button_pos = (screen_width - button_width - 10, 10 + offset_y)

        button_rect = pygame.Rect(button_pos[0], button_pos[1], button_width, button_height)
        return button_rect, button_text

    def render_button(self, button_rect, button_text):
        pygame.draw.rect(self.screen, WHITE, button_rect)
        self.screen.blit(button_text, (button_rect.x + 10, button_rect.y + 5))



    def draw_graph(self, node_values_ordered, edges, node_positions, scale):
        font_size = int(36 * scale)
        scaled_font = pygame.font.Font(None, font_size)

        for edge in edges:
            node1_pos = node_positions[edge[0]]
            node2_pos = node_positions[edge[1]]
            pygame.draw.line(self.screen, self.line_rgb, node1_pos, node2_pos, 2)

        for idx, node in enumerate(node_values_ordered):
            pos = node_positions[node]
            pygame.draw.circle(self.screen, self.node_rgb, pos, int(25 * scale))
            text = scaled_font.render(str(node), True, BLACK)
            text_rect = text.get_rect(center=pos)
            self.screen.blit(text, text_rect)


#_____________________________________________________________________________________________________________

def show_tkinter_popup(text):
    root = tk.Tk()
    root.withdraw()

    user_input = simpledialog.askstring("Input", text)
    
    root.destroy()

    return user_input


def pick_color(item_label, rgb_storage): 
    initial_color = (rgb_storage[0], rgb_storage[1], rgb_storage[2])
    
    color = colorchooser.askcolor(color=initial_color)[0]
    
    if color:
        hex_color = "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))
        
        item_label.config(bg=hex_color)
        
        rgb_storage[0], rgb_storage[1], rgb_storage[2] = int(color[0]), int(color[1]), int(color[2])
        print(f"RGB values for {item_label.cget('text')}: {rgb_storage}")

def apply_preset(item1_label, item2_label, item3_label, node_rgb, line_rgb, background_rgb):
    preset_node_rgb = list(WHITE)
    preset_line_rgb = list(WHITE)
    preset_background_rgb = list(BLACK)
    node_rgb[0], node_rgb[1], node_rgb[2] = preset_node_rgb
    line_rgb[0], line_rgb[1], line_rgb[2] = preset_line_rgb
    background_rgb[0], background_rgb[1], background_rgb[2] = preset_background_rgb

    item1_label.config(bg="#{:02x}{:02x}{:02x}".format(node_rgb[0], node_rgb[1], node_rgb[2]))
    item2_label.config(bg="#{:02x}{:02x}{:02x}".format(line_rgb[0], line_rgb[1], line_rgb[2]))
    item3_label.config(bg="#{:02x}{:02x}{:02x}".format(background_rgb[0], background_rgb[1], background_rgb[2]))

def color(node_rgb, line_rgb, background_rgb):
    root = tk.Tk()

    button1 = tk.Button(root, text="Pick Node Color", command=lambda: pick_color(item1_label, node_rgb))
    button1.pack(pady=5)

    item1_label = tk.Label(root, text="Node", width=20, height=2, bg="#{:02x}{:02x}{:02x}".format(node_rgb[0], node_rgb[1], node_rgb[2]))
    item1_label.pack(pady=10)

    button2 = tk.Button(root, text="Pick Line Color", command=lambda: pick_color(item2_label, line_rgb))
    button2.pack(pady=5)

    item2_label = tk.Label(root, text="Line", width=20, height=2, bg="#{:02x}{:02x}{:02x}".format(line_rgb[0], line_rgb[1], line_rgb[2]))
    item2_label.pack(pady=10)

    button3 = tk.Button(root, text="Pick Background Color", command=lambda: pick_color(item3_label, background_rgb))
    button3.pack(pady=5)

    item3_label = tk.Label(root, text="Background", width=20, height=2, bg="#{:02x}{:02x}{:02x}".format(background_rgb[0], background_rgb[1], background_rgb[2]))
    item3_label.pack(pady=10)

    preset_button = tk.Button(root, text="Apply Preset Colors", command=lambda: apply_preset(item1_label, item2_label, item3_label, node_rgb, line_rgb, background_rgb))
    preset_button.pack(pady=10)

    root.mainloop()
    
    return node_rgb, line_rgb, background_rgb

