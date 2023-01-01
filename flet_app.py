import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import flet
from flet import Page
from flet.matplotlib_chart import MatplotlibChart

import PID

matplotlib.use("svg")


def main(page: Page):
    def create(e):
        val, inc = PID.flet_api(
            float(start.value),
            float(in_goal.value),
            int(iterations.value),
            float(dt.value),
            float(max.value),
            float(min.value),
            float(kp.value),
            float(ki.value),
            float(kd.value),
        )
        ax.plot(val)
        ax.plot(inc)
        ax.set_xlabel("Iterations")
        ax.set_ylabel("Value & Increment")
        ax.grid(True)
        fig.tight_layout()
        chart = MatplotlibChart(fig, isolated=True,expand=True)
        page.add(chart)

    def remove(e):
        page.controls.pop(1)
        fig, ax = plt.subplots()
        page.update()    
        
    def update(e):
        val, inc = PID.flet_api(
            float(start.value),
            float(in_goal.value),
            int(iterations.value),
            float(dt.value),
            float(max.value),
            float(min.value),
            float(kp.value),
            float(ki.value),
            float(kd.value),
        )
        ax.plot(val)
        ax.plot(inc)
        chart.update()  

    btn_1 = flet.ElevatedButton("Erzeugen!", on_click=create)
    btn_2 = flet.ElevatedButton("Löschen!", on_click=remove)
    btn_3 = flet.ElevatedButton("Update!", on_click=update)
    
    fig, ax = plt.subplots()

    start = flet.TextField(label="Startwert", value="20", text_align="right", width=100)
    in_goal = flet.TextField(label="Zielwert", value="0", text_align="right", width=100)
    iterations = flet.TextField(
        label="Iterationen", value="100", text_align="right", width=100
    )
    dt = flet.TextField(label="dt", value="0.1", text_align="right", width=100)
    max = flet.TextField(label="Min", value="100", text_align="right", width=100)
    min = flet.TextField(label="Max", value="-100", text_align="right", width=100)
    kp = flet.TextField(label="kp", value="0.1", text_align="right", width=100)
    ki = flet.TextField(label="ki", value="0.5", text_align="right", width=100)
    kd = flet.TextField(label="kd", value="0.01", text_align="right", width=100)

    page.add(
        flet.Row(controls=
            [btn_1, btn_2, btn_3, start, in_goal, iterations, dt, max, min, kp, ki, kd]))


flet.app(target=main)
