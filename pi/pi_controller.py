import requests
import time
import random
import click
from sense_hat import SenseHat
sense = SenseHat()

def joy_direction():
    d_long = 0
    d_la = 0
    send_vel = False
    while True:
        for event in sense.stick.get_events():
            if event.action == "held" or event.action == "pressed":
                if event.direction =="up":
                    click.echo('Up')
                    send_vel = True
                    d_long = 0
                    d_la = 1   
                elif event.direction == "down":
                    click.echo('Up')
                    send_vel = True
                    d_long = 0
                    d_la = -1    
                elif event.direction == "left":
                    click.echo('Left')
                    send_vel = True
                    d_long = -1
                    d_la = 0
                elif event.direction == "right":
                    click.echo('Right')
                    send_vel = True
                    d_long = 1
                    d_la = 0
                else:
                    d_long = 0
                    d_la = 0
                    click.echo('Invalid input :(')
                    send_vel = False
                return d_long, d_la, send_vel
    
                    

def get_direction():
    d_long = 0
    d_la = 0
    send_vel = False
    c = click.getchar()
    if c =='a':
        click.echo('Left')
        send_vel = True
        d_long = -1
        d_la = 0
    elif c == 'd':
        click.echo('Right')
        send_vel = True
        d_long = 1
        d_la = 0
    elif c =='w':
        click.echo('Up')
        send_vel = True
        d_long = 0
        d_la = 1
    elif c == 's':
        click.echo('Down')
        send_vel = True
        d_long = 0
        d_la = -1
    else:
        d_long = 0
        d_la = 0
        click.echo('Invalid input :(')
        send_vel = False
    return d_long, d_la, send_vel


if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5000/drone"
    while True:
        d_long, d_la, send_vel = joy_direction()
        if send_vel:
            with requests.Session() as session:
                current_location = {'longitude': d_long,
                                    'latitude': d_la
                                    }
                resp = session.post(SERVER_URL, json=current_location)
