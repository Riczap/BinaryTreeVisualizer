import pygame
import math
import tkinter as tk
from tkinter import simpledialog
from tree import *
from widgets import *
from functions import *

#Global
WIDTH, HEIGHT = 800, 600

def preset_tree():
    btree = Tree()
    btree.head = Node(5)
    btree.insert(2)
    btree.insert(9)
    btree.insert(4)
    btree.insert(6)
    btree.insert(11)
    btree.insert(10)
    btree.insert(12)
    return btree


def preset_unbalanced():
    btree = Tree()
    btree.head = Node(5)
    btree.insert(2)
    btree.insert(9)
    btree.insert(4)
    btree.insert(6)
    btree.insert(11)
    btree.insert(10)
    btree.insert(12)
    btree.insert(13)
    btree.insert(3)
    return btree


create_preset_tree = True

btree = Tree()
if create_preset_tree:
    btree = preset_tree()
    node_values_ordered, edges, node_positions, scale = update_tree(btree)



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Binary Tree")
pygame.init()
render = Render(screen)
running = True
#Main Loop
#___________________________________________________________________________
while running:


    if not btree.head:
        empty_head = True
        while empty_head:
            user_input_value = show_tkinter_popup("New Tree Head Value")
            if not user_input_value:
                print("Canceled")
            else:
                btree.head = Node(int(user_input_value))
                node_values_ordered, edges, node_positions, scale = update_tree(btree)
                empty_head = False

    #Render and Create Objects
    #___________________________________________________________________________
    screen.fill(render.background_rgb)
    render.draw_graph(node_values_ordered, edges, node_positions, scale)

    button_rect1, button_text1 = render.create_button("Insert Node", WIDTH)
    render.render_button(button_rect1, button_text1)

    button_rect2, button_text2 = render.create_button("Delete Node", WIDTH, offset_y=40)
    render.render_button(button_rect2, button_text2)

    button_rect3, button_text3 = render.create_button("Clear Tree", WIDTH, offset_y=80)
    render.render_button(button_rect3, button_text3)

    button_rect4, button_text4 = render.create_button("Preset Tree", WIDTH, offset_y=120)
    render.render_button(button_rect4, button_text4)

    button_rect5, button_text5 = render.create_button("Balance Tree", WIDTH, offset_y=160)
    render.render_button(button_rect5, button_text5)

    button_rect6, button_text6 = render.create_button("Colors", WIDTH, offset_y=200)
    render.render_button(button_rect6, button_text6)

    render.balanced_text_box(btree.is_balanced())



    #Events
    #___________________________________________________________________________
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect1.collidepoint(event.pos):
                print("Insert Node")
                user_input_value = show_tkinter_popup("New Value")
                if not user_input_value:
                    print("Canceled")
                elif not int(user_input_value) in node_values_ordered:
                    btree.insert(int(user_input_value))
                    btree.tree_levels()
                    node_values_ordered, edges, node_positions, scale = update_tree(btree)
                else:
                    print("Enter a unique value")
            
            elif button_rect2.collidepoint(event.pos):
                print("Delete Node")
                user_input_value = show_tkinter_popup("Value to Delete")
                if not user_input_value:
                    print("Canceled")
                elif int(user_input_value) in node_values_ordered:
                    print(f"Node with value {int(user_input_value)} deleted")
                    btree.delete(int(user_input_value))
                    node_values_ordered, edges, node_positions, scale = update_tree(btree)
                else:
                    print("Node not found")

            elif button_rect3.collidepoint(event.pos):
                print("Clearing Tree")
                btree = Tree()
                node_values_ordered, edges, node_positions, scale = update_tree(btree)

            elif button_rect4.collidepoint(event.pos):
                print("Filling Tree")
                btree = preset_tree()
                node_values_ordered, edges, node_positions, scale = update_tree(btree)

            elif button_rect5.collidepoint(event.pos):
                print("Balancing Tree")
                btree = btree.balance_tree()
                node_values_ordered, edges, node_positions, scale = update_tree(btree)

            elif button_rect6.collidepoint(event.pos):
                print("Changing colors")
                render.node_rgb, render.line_rgb, render.background_rgb = color(render.node_rgb, render.line_rgb, render.background_rgb)
                node_values_ordered, edges, node_positions, scale = update_tree(btree)


    pygame.display.flip()

pygame.quit()
