import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import flet
from flet import Page
from flet.matplotlib_chart import MatplotlibChart

import PID

matplotlib.use("svg")


class PIDApp(flet.UserControl):
    def build(self):

        self.btn_3 = flet.ElevatedButton("Simulieren!", on_click=self.update)

        self.fig, self.ax = plt.subplots()
        self.chart = MatplotlibChart(self.fig, original_size=True)
        self.n = 1

        self.start = flet.TextField(
            label="Startwert", value="20", text_align="right", width=130
        )
        self.in_goal = flet.TextField(
            label="Zielwert", value="0", text_align="right", width=130
        )
        self.iterations = flet.TextField(
            label="Iterationen", value="100", text_align="right", width=130
        )
        self.dt = flet.TextField(
            label="dt (Zeitkonstante)", value="0.1", text_align="right", width=130
        )
        self.max = flet.TextField(
            label="Minimale Regelgröße", value="100", text_align="right", width=130
        )
        self.min = flet.TextField(
            label="Maximale Regelgröße", value="-100", text_align="right", width=130
        )
        self.kp = flet.TextField(
            label="kp (P-Anteil)", value="0.1", text_align="right", width=130
        )
        self.ki = flet.TextField(
            label="ki (I-Anteil)", value="0.5", text_align="right", width=130
        )
        self.kd = flet.TextField(
            label="kd (D-Anteil)", value="0.01", text_align="right", width=130
        )

        return [
            flet.Column(
                controls=[
                    flet.Row(
                        controls=[
                            self.btn_3,
                            self.start,
                            self.in_goal,
                            self.iterations,
                            self.max,
                            self.min,
                            self.kp,
                            self.ki,
                            self.kd,
                            self.dt,
                        ]
                    ),
                    self.chart,
                ]
            )
        ]

    def update(self, e):
        val, inc = PID.flet_api(
            float(self.start.value),
            float(self.in_goal.value),
            int(self.iterations.value),
            float(self.dt.value),
            float(self.max.value),
            float(self.min.value),
            float(self.kp.value),
            float(self.ki.value),
            float(self.kd.value),
        )
        self.ax.plot(val, label="Value " + str(self.n))
        self.ax.plot(inc, label="Increment " + str(self.n))
        self.ax.set_xlabel("Iterations")
        self.ax.set_ylabel("Value & Increment")
        self.ax.legend()
        self.ax.grid(True)
        self.fig.tight_layout()
        self.chart.update()
        self.n += 1


def main(page: Page):
    def remove(e):
        if len(page.controls) <= 2:
            return
        else:
            page.controls.pop()
            page.update()

    def create(e):
        app = PIDApp()
        page.add(app)
        page.update()

    page.title = "PID App"
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    btn_1 = flet.ElevatedButton("Erzeugen!", on_click=create)
    btn_2 = flet.ElevatedButton("Löschen!", on_click=remove)
    txt = flet.Text(value="Simulieren Sie einen Regler:   ")
    page.add(flet.Row(controls=[txt, btn_1, btn_2]), flet.Divider())
    page.update()


if __name__ == "__main__":
    flet.app(target=main)
